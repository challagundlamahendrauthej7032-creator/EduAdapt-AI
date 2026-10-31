"""
EduAdapt AI - Diagnostic Test View
5 Multiple-Choice Questions covering core Class 10 Physics topics.
Calculates score, diagnoses weak concepts, updates learner model,
and delivers detailed post-answer feedback.
"""

import streamlit as st
from data.physics_questions import DIAGNOSTIC_QUESTIONS
from components.ui_helpers import render_hero, render_feedback_card, render_status_pill


def render_diagnostic_test(learner_model):
    """Renders the 5-question Physics Diagnostic Test and results summary."""
    render_hero(
        title="Diagnostic Assessment 📝",
        subtitle="5 High-Yield Questions designed to pinpoint your Class 10 Physics mastery and uncover misconceptions.",
        tag="Diagnostic Evaluation • 5 MCQs"
    )

    # Initialize answers in session state if needed
    if "diag_user_answers" not in st.session_state:
        st.session_state["diag_user_answers"] = {}

    # Check if test was previously submitted
    if learner_model.diagnostic_completed:
        _render_diagnostic_results(learner_model)
        return

    st.markdown("""
    > 💡 **Instructions:** Answer all 5 questions carefully. Take your time to calculate numerical values using paper and pen. Once submitted, EduAdapt AI will compute your score, map your concept mastery, and generate targeted adaptive practice.
    """)

    # Render each of the 5 diagnostic questions
    user_selections = {}
    
    for i, q in enumerate(DIAGNOSTIC_QUESTIONS):
        qid = q["id"]
        cname = q["concept_name"]
        
        st.markdown(f"""
        <div class="question-box">
            <span class="question-tag">Question {i+1} of 5 • {cname}</span>
            <div style="font-size: 1.05rem; font-weight: 600; color: #1e293b; margin-bottom: 0.8rem;">
                {q['question']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Radio options
        selected_option = st.radio(
            label=f"Select your answer for Question {i+1}:",
            options=q["options"],
            key=f"diag_radio_{qid}",
            index=None,
            label_visibility="collapsed"
        )

        # Extract selected index (0, 1, 2, or 3)
        if selected_option:
            selected_idx = q["options"].index(selected_option)
            user_selections[qid] = selected_idx
        else:
            user_selections[qid] = -1

        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    # Submission Row
    col1, col2 = st.columns([1, 2])
    with col1:
        answered_count = sum(1 for v in user_selections.values() if v != -1)
        st.write(f"**Answered:** {answered_count} / {len(DIAGNOSTIC_QUESTIONS)}")

    with col2:
        submit_clicked = st.button("🚀 Submit Diagnostic Test & View AI Analysis", type="primary", use_container_width=True)

    if submit_clicked:
        if answered_count < len(DIAGNOSTIC_QUESTIONS):
            st.error(f"Please answer all 5 questions before submitting. (You have answered {answered_count}/5)")
        else:
            with st.spinner("Analyzing answers and updating Learner Model..."):
                results = learner_model.process_diagnostic_results(user_selections, DIAGNOSTIC_QUESTIONS)
                st.session_state["diag_user_answers"] = user_selections
                st.rerun()


def _render_diagnostic_results(learner_model):
    """Displays score, weak concepts diagnosis, and detailed step-by-step feedback."""
    score = learner_model.diagnostic_score
    total = learner_model.diagnostic_total
    pct = int((score / total) * 100)
    weak_count = len(learner_model.weak_concepts)

    if score >= 4:
        st.balloons()

    # Results Header Card
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; border-radius: 16px; padding: 1.8rem; margin-bottom: 1.5rem; border: 1px solid #334155;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <span style="background: #3b82f6; color: white; padding: 0.2rem 0.6rem; border-radius: 999px; font-size: 0.75rem; font-weight: 700;">DIAGNOSTIC RESULT</span>
                <h2 style="color: white; margin: 0.5rem 0 0.2rem 0; font-size: 2rem;">Diagnostic Score: {score} / {total} ({pct}%)</h2>
                <p style="color: #94a3b8; margin: 0;">{"Outstanding conceptual strength! Minor polishing required." if score >= 4 else "Foundational diagnostic complete. Weak concepts flagged for immediate revision."}</p>
            </div>
            <div style="text-align: right; margin-top: 0.8rem;">
                <div style="font-size: 2.2rem; font-weight: 800; color: {'#10b981' if score >= 4 else '#f59e0b' if score >= 3 else '#ef4444'};">{pct}%</div>
                <div style="font-size: 0.85rem; color: #cbd5e1;">{'Proficient' if score >= 4 else 'Developing' if score >= 3 else 'Needs Focus'}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Summary metrics row
    res_c1, res_c2, res_c3 = st.columns(3)
    with res_c1:
        st.metric(label="✅ Correct Answers", value=f"{score} / {total}")
    with res_c2:
        st.metric(label="❌ Identified Weak Concepts", value=str(weak_count), delta=f"{weak_count} to fix" if weak_count > 0 else "None!", delta_color="inverse")
    with res_c3:
        st.metric(label="📈 Post-Diagnostic Readiness", value=f"{learner_model.get_overall_readiness_score()}%")

    st.markdown("---")

    # Post-Diagnostic Action Banner
    if weak_count > 0:
        st.warning(f"⚠️ **EduAdapt AI identified {weak_count} weak concept{'s' if weak_count > 1 else ''} needing reinforcement:**")
        cols = st.columns(weak_count)
        for idx, cid in enumerate(learner_model.weak_concepts):
            with cols[idx % len(cols)]:
                from config import CONCEPT_MAP
                c_data = CONCEPT_MAP.get(cid, {})
                st.markdown(f"**{c_data.get('icon', '📌')} {c_data.get('name', cid)}**")
                st.caption(f"Mastery: {int(learner_model.concept_mastery.get(cid, 35))}%")

        if st.button("🎯 Launch Adaptive Practice on Weak Concepts Now", type="primary", use_container_width=True):
            st.session_state["nav_selection"] = "Adaptive Practice"
            st.session_state["selected_practice_concept"] = learner_model.weak_concepts[0]
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Step-by-Step Question Audit with Useful Feedback (Requirement 10)
    st.subheader("📋 Step-by-Step Answer Review & Explanations")
    for i, detail in enumerate(learner_model.diagnostic_details):
        is_corr = detail["is_correct"]
        q_num = i + 1
        icon = "✅" if is_corr else "❌"
        status_label = "Correct" if is_corr else "Incorrect"
        
        with st.expander(f"{icon} Question {q_num}: {detail['concept_name']} — {status_label}", expanded=not is_corr):
            st.markdown(f"**Question:** {detail['question_text']}")
            
            # Find original question for options
            orig_q = next((q for q in DIAGNOSTIC_QUESTIONS if q["id"] == detail["question_id"]), None)
            if orig_q:
                st.markdown("**Options:**")
                for opt_idx, opt in enumerate(orig_q["options"]):
                    if opt_idx == orig_q["correct_index"]:
                        st.markdown(f"- **{opt}** *(Correct Answer)* ✅")
                    elif opt_idx == detail["selected_index"]:
                        st.markdown(f"- **{opt}** *(Your Choice)* ❌")
                    else:
                        st.markdown(f"- {opt}")

            # Extract why wrong if incorrect
            selected_letter = chr(65 + detail["selected_index"]) if 0 <= detail["selected_index"] < 4 else "None"
            why_wrong_msg = orig_q["why_wrong"].get(selected_letter, "") if orig_q else ""

            # Render full feedback card
            render_feedback_card(
                is_correct=is_corr,
                explanation=detail["explanation"],
                formula=detail["formula"],
                why_wrong=why_wrong_msg,
                board_tip=detail["board_tip"]
            )

    st.markdown("---")
    # Retake Option
    if st.button("🔄 Retake Diagnostic Test (Reset Answers)", type="secondary"):
        learner_model.diagnostic_completed = False
        learner_model.diagnostic_score = 0
        learner_model.diagnostic_details = []
        st.session_state["diag_user_answers"] = {}
        st.rerun()
