"""
EduAdapt AI - Adaptive Practice Engine
Generates targeted questions based on the student's weak concepts and mastery level.
Delivers instant, useful feedback and adjusts mastery in real-time.
"""

import streamlit as st
from config import CONCEPTS, CONCEPT_MAP, MASTERY_THRESHOLDS
from data.physics_questions import PRACTICE_QUESTIONS
from components.ui_helpers import render_hero, render_feedback_card, render_status_pill


def render_adaptive_practice(learner_model):
    """Renders the Adaptive Practice interface."""
    render_hero(
        title="Adaptive Practice Engine 🎯",
        subtitle="AI-curated Physics problems targeting your identified weak concepts and auto-calibrated to your skill tier.",
        tag="Adaptive Learning • Weak Concept Remediation"
    )

    # Session state initialization for practice workflow
    if "current_practice_q_idx" not in st.session_state:
        st.session_state["current_practice_q_idx"] = 0
    if "practice_submitted" not in st.session_state:
        st.session_state["practice_submitted"] = False
    if "last_practice_result" not in st.session_state:
        st.session_state["last_practice_result"] = None

    # Top Bar: Focus Concept Selection
    weak_concepts = learner_model.weak_concepts
    
    # Preset selection if coming from another view
    default_concept_idx = 0
    concept_options = [c["id"] for c in CONCEPTS]
    concept_display = {c["id"]: f"{c['icon']} {c['name']} ({int(learner_model.concept_mastery.get(c['id'], 50))}% Mastery)" for c in CONCEPTS}

    if "selected_practice_concept" in st.session_state and st.session_state["selected_practice_concept"] in concept_options:
        default_concept_idx = concept_options.index(st.session_state["selected_practice_concept"])
    elif weak_concepts:
        default_concept_idx = concept_options.index(weak_concepts[0])

    col_sel1, col_sel2 = st.columns([2, 1])

    with col_sel1:
        selected_cid = st.selectbox(
            "Select Concept to Practice:",
            options=concept_options,
            index=default_concept_idx,
            format_func=lambda x: concept_display[x]
        )
        st.session_state["selected_practice_concept"] = selected_cid

    curr_mastery = learner_model.concept_mastery.get(selected_cid, 50.0)
    recommended_diff = learner_model.get_recommended_difficulty(selected_cid)

    with col_sel2:
        diff_choice = st.selectbox(
            "Difficulty Tier:",
            options=["Adaptive (AI Recommended)", "Easy", "Medium", "Hard"],
            index=0,
            help="Adaptive automatically chooses based on your current concept mastery."
        )

    if diff_choice == "Adaptive (AI Recommended)":
        target_diff = recommended_diff
        diff_note = f"🤖 AI Selected: **{recommended_diff}** based on your {curr_mastery:.0f}% mastery"
    else:
        target_diff = diff_choice
        diff_note = f"Manual override: **{target_diff}**"

    st.caption(diff_note)

    # Fetch questions for selected concept
    c_questions = PRACTICE_QUESTIONS.get(selected_cid, [])
    
    # Filter by difficulty if available, else fallback
    matching_q = [q for q in c_questions if q.get("difficulty") == target_diff]
    if not matching_q:
        matching_q = c_questions

    if not matching_q:
        st.info("No practice questions found for this selection.")
        return

    # Choose question based on index
    q_idx = st.session_state["current_practice_q_idx"] % len(matching_q)
    question = matching_q[q_idx]

    st.markdown("---")

    # Main Question & Sidebar Tracker Layout
    main_col, stats_col = st.columns([3, 1])

    with main_col:
        c_meta = CONCEPT_MAP.get(selected_cid, {})
        status_str = learner_model.get_concept_status(selected_cid)

        # Question Header Box
        st.markdown(f"""
        <div class="question-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
                <span class="question-tag">{c_meta.get('icon', '📌')} {c_meta.get('name', 'Physics')}</span>
                <span style="font-size: 0.8rem; font-weight: 700; background: #f1f5f9; padding: 0.2rem 0.6rem; border-radius: 6px; color: #475569;">
                    Difficulty: {question.get('difficulty', 'Medium')}
                </span>
            </div>
            <div style="font-size: 1.15rem; font-weight: 600; color: #0f172a; line-height: 1.5; margin-bottom: 1rem;">
                {question['question']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # If not submitted, show options and submit button
        if not st.session_state["practice_submitted"]:
            selected_option = st.radio(
                label="Choose the correct answer:",
                options=question["options"],
                index=None,
                key=f"prac_opt_{question['id']}_{st.session_state['current_practice_q_idx']}"
            )

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                if st.button("✅ Check Answer & View Feedback", type="primary", use_container_width=True):
                    if selected_option is None:
                        st.warning("Please select an option before checking.")
                    else:
                        selected_idx = question["options"].index(selected_option)
                        # Record in learner model
                        result_entry = learner_model.record_practice_answer(question, selected_idx)
                        st.session_state["practice_submitted"] = True
                        st.session_state["last_practice_result"] = result_entry
                        st.rerun()

            with btn_col2:
                if st.button("⏭️ Skip to Next Question", use_container_width=True):
                    st.session_state["current_practice_q_idx"] += 1
                    st.session_state["practice_submitted"] = False
                    st.rerun()

        # If submitted, show feedback and next button
        else:
            result = st.session_state["last_practice_result"]
            is_corr = result["is_correct"]
            sel_idx = result["selected_index"]

            # Display which option was picked
            for o_idx, opt in enumerate(question["options"]):
                if o_idx == question["correct_index"]:
                    st.markdown(f"- **{opt}** *(Correct)* ✅")
                elif o_idx == sel_idx:
                    st.markdown(f"- **{opt}** *(Your Answer)* ❌")
                else:
                    st.markdown(f"- {opt}")

            # Feedback Card
            sel_letter = chr(65 + sel_idx) if 0 <= sel_idx < 4 else "None"
            why_wrong = question["why_wrong"].get(sel_letter, "")

            render_feedback_card(
                is_correct=is_corr,
                explanation=question["explanation"],
                formula=question.get("formula", ""),
                why_wrong=why_wrong,
                board_tip=question.get("board_tip", "")
            )

            # Show Mastery Adjustment
            delta_val = result['new_mastery'] - result['old_mastery']
            sign = "+" if delta_val > 0 else ""
            delta_color = "green" if delta_val > 0 else "red"
            st.markdown(f"""
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 0.8rem 1rem; margin: 0.8rem 0;">
                <b>📈 Dynamic Mastery Update:</b> {c_meta.get('short_name', 'Concept')} mastery shifted from 
                <b>{result['old_mastery']:.0f}%</b> ➔ <b>{result['new_mastery']:.0f}%</b> 
                (<span style="color: {delta_color}; font-weight: bold;">{sign}{delta_val:.1f}%</span>)
            </div>
            """, unsafe_allow_html=True)

            # Next Question Button
            if st.button("🚀 Practice Next Adaptive Question", type="primary", use_container_width=True):
                st.session_state["current_practice_q_idx"] += 1
                st.session_state["practice_submitted"] = False
                st.session_state["last_practice_result"] = None
                st.rerun()

    with stats_col:
        st.markdown("### 📊 Live Mastery")
        st.metric(
            label="Current Concept Mastery",
            value=f"{curr_mastery:.0f}%",
            delta=learner_model.get_concept_status(selected_cid)
        )

        st.markdown(f"**Status:** {render_status_pill(status_str)}", unsafe_allow_html=True)
        st.write(f"**Recommended Tier:** `{recommended_diff}`")

        st.markdown("---")
        st.markdown("### 📐 Quick Formulas")
        for f in c_meta.get("key_formulas", [])[:3]:
            st.code(f, language="text")

        st.markdown("---")
        st.write(f"**Total Solved:** {learner_model.total_questions_solved}")
        st.write(f"**Correct:** {learner_model.total_correct_count}")
        if learner_model.total_questions_solved > 0:
            acc = int((learner_model.total_correct_count / learner_model.total_questions_solved) * 100)
            st.write(f"**Accuracy:** `{acc}%`")
