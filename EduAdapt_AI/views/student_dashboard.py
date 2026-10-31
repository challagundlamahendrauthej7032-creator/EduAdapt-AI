"""
EduAdapt AI - Student Dashboard View
Main landing screen showing learner readiness, concept mastery breakdown,
weak concept alerts, and quick study actions.
"""

from datetime import datetime
import streamlit as st
from config import CONCEPTS, CONCEPT_MAP, BOARD_EXAM_DATE
from components.ui_helpers import render_hero, render_metric_card, render_status_pill
from components.charts import create_mastery_bar_chart


def render_student_dashboard(learner_model):
    """Renders the comprehensive Student Dashboard."""
    # Days to board exam calculation
    try:
        exam_dt = datetime.strptime(BOARD_EXAM_DATE, "%Y-%m-%d")
        days_left = (exam_dt - datetime.now()).days
        days_str = f"{max(1, days_left)} Days"
    except Exception:
        days_str = "120 Days"

    readiness = learner_model.get_overall_readiness_score()
    diag_done = learner_model.diagnostic_completed
    weak_count = len(learner_model.weak_concepts)

    # Hero Banner
    render_hero(
        title=f"Welcome back, {learner_model.student_name}! 🚀",
        subtitle="Your personalized AI tutor for Class 10 CBSE Physics Board Exam mastery.",
        tag="Student Dashboard • Physics Exam-Prep"
    )

    # KPI Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        delta_label = "+5% this week" if diag_done else "Baseline"
        st.metric(
            label="🎯 Board Exam Readiness",
            value=f"{readiness}%",
            delta=delta_label
        )

    with col2:
        if diag_done:
            diag_val = f"{learner_model.diagnostic_score} / 5"
            diag_caption = f"Completed ({int((learner_model.diagnostic_score/5)*100)}%)"
        else:
            diag_val = "Pending"
            diag_caption = "Take test to baseline"
        st.metric(
            label="📝 Diagnostic Test",
            value=diag_val,
            delta="Ready" if not diag_done else "Done",
            delta_color="normal" if not diag_done else "inverse"
        )

    with col3:
        weak_val = str(weak_count)
        weak_caption = "Need reinforcement" if weak_count > 0 else "All concepts healthy"
        st.metric(
            label="⚠️ Weak Concepts",
            value=weak_val,
            delta=f"{weak_count} flagged" if weak_count > 0 else "Zero weak topics!",
            delta_color="inverse" if weak_count > 0 else "normal"
        )

    with col4:
        st.metric(
            label="⏳ CBSE Board Exam",
            value=days_str,
            delta=f"🔥 {learner_model.study_streak_days} Day Streak"
        )

    st.markdown("---")

    # Quick Navigation / Action Bar
    st.subheader("⚡ Quick Actions")
    act_col1, act_col2, act_col3, act_col4 = st.columns(4)

    with act_col1:
        if st.button("📝 Take Diagnostic Test", use_container_width=True, type="primary" if not diag_done else "secondary"):
            st.session_state["nav_selection"] = "Diagnostic Test (5 MCQs)"
            st.rerun()

    with act_col2:
        if st.button("🎯 Practice Weak Concepts", use_container_width=True, type="primary" if (diag_done and weak_count > 0) else "secondary"):
            st.session_state["nav_selection"] = "Adaptive Practice"
            st.rerun()

    with act_col3:
        if st.button("📅 View Revision Planner", use_container_width=True):
            st.session_state["nav_selection"] = "Revision Schedule"
            st.rerun()

    with act_col4:
        if st.button("🎙️ Wispr Flow Voice Practice", use_container_width=True):
            st.session_state["nav_selection"] = "Wispr Flow Voice Dictation"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Two column layout: Left = Mastery Chart, Right = Weak Concept Diagnostics
    left_col, right_col = st.columns([3, 2])

    with left_col:
        st.subheader("📊 Concept Mastery Tracking")
        chart = create_mastery_bar_chart(learner_model.concept_mastery)
        st.altair_chart(chart, use_container_width=True)

        st.caption("💡 *Mastery updates dynamically with every diagnostic and adaptive practice question answered.*")

    with right_col:
        st.subheader("🔍 Weak Concept Diagnostic")
        if weak_count == 0:
            st.success("🌟 **Great job!** No concepts currently flagged as weak. Keep up the consistent revision to maintain mastery above 80%.")
            st.info("Tip: Challenge yourself with **Hard** numerical problems in the Adaptive Practice section!")
        else:
            st.warning(f"⚠️ **{weak_count} Concept{'s' if weak_count > 1 else ''} Need Attention:**")
            for cid in learner_model.weak_concepts:
                c_info = CONCEPT_MAP.get(cid, {})
                c_mastery = learner_model.concept_mastery.get(cid, 0)
                
                with st.expander(f"{c_info.get('icon', '📌')} {c_info.get('name', cid)} — {c_mastery}%", expanded=True):
                    st.write(f"**Status:** {render_status_pill('Needs Focus')}", unsafe_allow_html=True)
                    st.write(f"**Syllabus Weightage:** {c_info.get('weight', 20)}%")
                    
                    # Display identified misconceptions if any
                    misconceptions = learner_model.identified_misconceptions.get(cid, [])
                    if misconceptions:
                        st.markdown("**Identified Misconception:**")
                        for m in set(misconceptions):
                            st.caption(f"• {m}")
                    
                    # Key Formulas
                    st.markdown("**Essential Formulas to Memorize:**")
                    for f in c_info.get("key_formulas", [])[:2]:
                        st.code(f, language="text")

                    if st.button(f"Generate Practice for {c_info.get('short_name', 'Topic')}", key=f"btn_prac_{cid}"):
                        st.session_state["nav_selection"] = "Adaptive Practice"
                        st.session_state["selected_practice_concept"] = cid
                        st.rerun()

    st.markdown("---")

    # Class 10 Syllabus Overview Cards
    st.subheader("📚 Class 10 Physics Syllabus Status")
    syl_cols = st.columns(len(CONCEPTS))
    for i, c in enumerate(CONCEPTS):
        cid = c["id"]
        mastery = learner_model.concept_mastery.get(cid, 50.0)
        status = learner_model.get_concept_status(cid)
        
        with syl_cols[i]:
            st.markdown(f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1rem; text-align: center; min-height: 170px;">
                <div style="font-size: 1.8rem;">{c['icon']}</div>
                <div style="font-size: 0.85rem; font-weight: 700; margin: 0.4rem 0; color: #1e293b;">{c['short_name']}</div>
                <div style="font-size: 1.3rem; font-weight: 800; color: #3b82f6;">{int(mastery)}%</div>
                <div style="margin-top: 0.4rem;">{render_status_pill(status)}</div>
            </div>
            """, unsafe_allow_html=True)
