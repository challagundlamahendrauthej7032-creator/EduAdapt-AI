"""
EduAdapt AI - Adaptive Exam-Prep Tutor with Learner Model
Target: Class 10 Physics (CBSE / ICSE)
Main Application Entrypoint
"""

import streamlit as st

# Configure Streamlit page settings
st.set_page_config(
    page_title="EduAdapt AI • Class 10 Physics",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from config import APP_NAME, APP_SUBTITLE
from models.learner_model import LearnerModel
from components.ui_helpers import apply_custom_css, render_status_pill
from views.student_dashboard import render_student_dashboard
from views.diagnostic_test import render_diagnostic_test
from views.adaptive_practice import render_adaptive_practice
from views.revision_planner import render_revision_planner
from views.voice_dictation import render_voice_dictation_view
from views.teacher_dashboard import render_teacher_dashboard


def init_session_state():
    """Initialize global learner model and navigation state."""
    if "learner_model" not in st.session_state:
        st.session_state["learner_model"] = LearnerModel(student_name="Aarav Sharma")
    if "nav_selection" not in st.session_state:
        st.session_state["nav_selection"] = "Student Dashboard"


def main():
    apply_custom_css()
    init_session_state()

    learner_model = st.session_state["learner_model"]

    # ---------------------------------------------
    # SIDEBAR NAVIGATION & STUDENT PROFILE
    # ---------------------------------------------
    with st.sidebar:
        st.markdown(f"""
        <div style="padding: 0.6rem 0.2rem 1.2rem 0.2rem; border-bottom: 1px solid #334155; margin-bottom: 1.2rem;">
            <div style="font-size: 1.6rem; font-weight: 800; color: #ffffff; display: flex; align-items: center; gap: 8px;">
                <span>⚛️</span> {APP_NAME}
            </div>
            <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 0.3rem;">
                Adaptive Exam-Prep Tutor • Class 10 Physics
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Navigation Options
        nav_options = [
            "Student Dashboard",
            "Diagnostic Test (5 MCQs)",
            "Adaptive Practice",
            "Revision Schedule",
            "Wispr Flow Voice Dictation",
            "Teacher Dashboard"
        ]

        # Sync nav selection
        current_nav = st.session_state.get("nav_selection", "Student Dashboard")
        if current_nav not in nav_options:
            current_nav = "Student Dashboard"

        nav_index = nav_options.index(current_nav)

        selected_page = st.radio(
            label="NAVIGATION",
            options=nav_options,
            index=nav_index,
            format_func=lambda x: {
                "Student Dashboard": "🏠 Student Dashboard",
                "Diagnostic Test (5 MCQs)": "📝 Diagnostic Test (5 MCQs)",
                "Adaptive Practice": "🎯 Adaptive Practice",
                "Revision Schedule": "📅 Revision Schedule",
                "Wispr Flow Voice Dictation": "🎙️ Wispr Flow Voice Dictation",
                "Teacher Dashboard": "👨‍🏫 Teacher Dashboard"
            }.get(x, x)
        )

        st.session_state["nav_selection"] = selected_page

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")

        # Student Status Widget in Sidebar
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 1rem; margin-bottom: 1rem;">
            <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 700; letter-spacing: 0.05em;">ACTIVE LEARNER</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin: 0.2rem 0;">Aarav Sharma</div>
            <div style="font-size: 0.8rem; color: #cbd5e1;">Class 10-A • CBSE Board</div>
        </div>
        """, unsafe_allow_html=True)

        readiness = learner_model.get_overall_readiness_score()
        st.write(f"**Board Readiness:** `{readiness}%`")
        st.progress(readiness / 100.0)

        weak_cnt = len(learner_model.weak_concepts)
        if weak_cnt > 0:
            st.warning(f"⚠️ {weak_cnt} Weak Concept{'s' if weak_cnt > 1 else ''} Identified")
        else:
            st.success("✅ Zero Weak Concepts")

        st.markdown("<br>", unsafe_allow_html=True)

        # Demo Reset Button
        if st.button("🔄 Reset Demo / Re-baseline", use_container_width=True, help="Resets student answers and baseline mastery"):
            learner_model.reset_model()
            st.session_state["diag_user_answers"] = {}
            st.session_state["current_practice_q_idx"] = 0
            st.session_state["practice_submitted"] = False
            st.session_state["last_practice_result"] = None
            st.toast("Learner model reset to baseline!", icon="🔄")
            st.rerun()

        st.markdown("""
        <div style="font-size: 0.72rem; color: #64748b; text-align: center; margin-top: 1.5rem;">
            EduAdapt AI v1.0 • Built with Streamlit & Wispr Flow
        </div>
        """, unsafe_allow_html=True)

    # ---------------------------------------------
    # VIEW ROUTING
    # ---------------------------------------------
    if selected_page == "Student Dashboard":
        render_student_dashboard(learner_model)

    elif selected_page == "Diagnostic Test (5 MCQs)":
        render_diagnostic_test(learner_model)

    elif selected_page == "Adaptive Practice":
        render_adaptive_practice(learner_model)

    elif selected_page == "Revision Schedule":
        render_revision_planner(learner_model)

    elif selected_page == "Wispr Flow Voice Dictation":
        render_voice_dictation_view(learner_model)

    elif selected_page == "Teacher Dashboard":
        render_teacher_dashboard()


if __name__ == "__main__":
    main()
