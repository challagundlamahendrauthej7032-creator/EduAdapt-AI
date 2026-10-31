"""
EduAdapt AI - Wispr Flow Voice Dictation View
Allows students to dictate conceptual physics answers using Wispr Flow voice dictation.
Evaluates spoken clarity, scientific keyword usage, and conceptual completeness.
"""

import streamlit as st
from data.physics_questions import VOICE_CHALLENGES
from components.ui_helpers import render_hero
from components.voice_component import render_wispr_flow_mic_widget, evaluate_voice_answer


def render_voice_dictation_view(learner_model):
    """Renders the Wispr Flow Voice Dictation practice module."""
    render_hero(
        title="Wispr Flow Voice Dictation Studio 🎙️",
        subtitle="Practice explaining Class 10 Physics concepts out loud. Wispr Flow transcribes your speech and analyzes your conceptual precision.",
        tag="Voice-First Learning • Wispr Flow Integration"
    )

    # Info card on Feynman Technique / Wispr Flow
    with st.expander("💡 Why Voice Dictation with Wispr Flow?", expanded=False):
        st.markdown("""
        - **The Feynman Technique:** Explaining concepts aloud in your own words is proven to build the deepest conceptual retention.
        - **Board Exam Answer Quality:** Class 10 Board examiners look for specific scientific vocabulary and clear cause-and-effect reasoning.
        - **Wispr Flow Voice Engine:** Transcribe your voice effortlessly, check your scientific vocabulary coverage, and compare against model board answers.
        """)

    # Select Voice Challenge
    challenge_titles = [c["title"] for c in VOICE_CHALLENGES]
    selected_title = st.selectbox(
        "Select Conceptual Physics Topic to Dictate:",
        options=challenge_titles,
        index=0
    )

    challenge = next(c for c in VOICE_CHALLENGES if c["title"] == selected_title)

    # Question Prompt Card
    st.markdown(f"""
    <div style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 6px solid #8b5cf6; border-radius: 14px; padding: 1.4rem; margin-bottom: 1.2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
            <span style="background: #ede9fe; color: #6d28d9; padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.78rem; font-weight: 700;">
                TOPIC: {challenge['title'].upper()}
            </span>
            <span style="font-size: 0.8rem; font-weight: 600; color: #64748b;">
                Difficulty: {challenge['difficulty']}
            </span>
        </div>
        <div style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin-bottom: 0.6rem;">
            {challenge['prompt']}
        </div>
        <div style="font-size: 0.85rem; color: #64748b;">
            <b>Key Physics Concepts to Include:</b> {', '.join(challenge['expected_keywords'][:5])}...
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. Real-time Live Microphone Web Speech API Component
    st.markdown("### 1. Speak via Wispr Flow Dictation")
    render_wispr_flow_mic_widget(target_element_id="wispr_dictation_box")

    st.markdown("<br>", unsafe_allow_html=True)

    # Session state for the dictated transcript text
    text_key = f"voice_transcript_{challenge['id']}"
    if text_key not in st.session_state:
        st.session_state[text_key] = ""

    # Quick Simulation Presets for immediate testing
    st.markdown("### 2. Dictated Transcript")
    st.caption("Paste your transcribed audio above, or click a Quick Voice preset below to simulate spoken Wispr Flow input:")

    sim_col1, sim_col2, sim_col3 = st.columns(3)
    with sim_col1:
        if st.button("🗣️ Simulate: Ideal Verbal Answer", key=f"sim_good_{challenge['id']}", use_container_width=True):
            st.session_state[text_key] = challenge["sample_good_dictation"]
            st.rerun()

    with sim_col2:
        if st.button("🗣️ Simulate: Partial Verbal Answer", key=f"sim_partial_{challenge['id']}", use_container_width=True):
            st.session_state[text_key] = "It depends on the angle of incidence and light changes direction when moving from air to glass."
            st.rerun()

    with sim_col3:
        if st.button("🧹 Clear Input", key=f"sim_clear_{challenge['id']}", use_container_width=True):
            st.session_state[text_key] = ""
            st.rerun()

    # User Answer Text Area
    user_transcript = st.text_area(
        label="Dictated Answer Text (transcribed from voice):",
        value=st.session_state[text_key],
        height=130,
        placeholder="Your spoken words transcribed by Wispr Flow will appear here. You can also edit or refine them...",
        key=f"area_{challenge['id']}"
    )

    # Submission & Evaluation
    if st.button("🚀 Analyze Spoken Answer with EduAdapt AI", type="primary", use_container_width=True):
        if not user_transcript or len(user_transcript.strip()) < 5:
            st.warning("Please dictate or enter an explanation before analyzing.")
        else:
            with st.spinner("Analyzing semantic physics keywords, conceptual completeness, and clarity..."):
                eval_res = evaluate_voice_answer(
                    transcript=user_transcript,
                    expected_keywords=challenge["expected_keywords"],
                    ideal_explanation=challenge["ideal_explanation"]
                )
                
                # Save into learner model
                learner_model.record_voice_attempt(challenge, user_transcript, eval_res)
                st.session_state[f"eval_{challenge['id']}"] = eval_res
                st.rerun()

    # Display Evaluation Results if available
    eval_state_key = f"eval_{challenge['id']}"
    if eval_state_key in st.session_state:
        eval_data = st.session_state[eval_state_key]
        score = eval_data["score"]

        st.markdown("---")
        st.subheader("📊 Wispr Flow Voice Answer Analysis")

        # Result Banner
        tier_color = "#10b981" if score >= 75 else "#f59e0b" if score >= 50 else "#ef4444"
        st.markdown(f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-left: 6px solid {tier_color}; border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size: 0.8rem; font-weight: 700; color: #64748b;">EVALUATION SCORE</span>
                    <h3 style="margin: 0.2rem 0; color: #0f172a;">{eval_data['clarity_tier']}</h3>
                    <p style="margin: 0; color: #475569; font-size: 0.95rem;">{eval_data['feedback']}</p>
                </div>
                <div style="font-size: 2.2rem; font-weight: 800; color: {tier_color};">
                    {score}%
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Keyword Breakdown
        kw_col1, kw_col2 = st.columns(2)
        with kw_col1:
            st.markdown("**✅ Scientific Keywords Captured:**")
            if eval_data["matched_keywords"]:
                matched_html = " ".join([f"<span style='display: inline-block; background: #d1fae5; color: #065f46; font-size: 0.8rem; font-weight: 600; padding: 3px 8px; border-radius: 6px; margin: 2px;'>✓ {kw}</span>" for kw in eval_data["matched_keywords"]])
                st.markdown(matched_html, unsafe_allow_html=True)
            else:
                st.caption("No key scientific terms detected.")

        with kw_col2:
            st.markdown("**⚠️ Key Terms Missing in Dictation:**")
            if eval_data["missing_keywords"]:
                missing_html = " ".join([f"<span style='display: inline-block; background: #fee2e2; color: #991b1b; font-size: 0.8rem; font-weight: 600; padding: 3px 8px; border-radius: 6px; margin: 2px;'>✗ {kw}</span>" for kw in eval_data["missing_keywords"]])
                st.markdown(missing_html, unsafe_allow_html=True)
            else:
                st.caption("None! All essential terminology captured.")

        st.markdown("<br>", unsafe_allow_html=True)

        # Model Answer Comparison
        st.markdown("""
        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 1.1rem; margin-top: 0.8rem;">
            <b style="color: #1e293b; font-size: 0.95rem;">🏆 Ideal Class 10 Board Exam Model Explanation:</b>
            <div style="margin-top: 0.5rem; font-size: 0.9rem; line-height: 1.6; color: #334155;">
        """ + challenge["ideal_explanation"] + """
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Previous Voice Attempts
    if learner_model.voice_history:
        st.markdown("---")
        st.subheader("📜 Recent Voice Dictation History")
        for attempt in reversed(learner_model.voice_history[-3:]):
            st.markdown(f"""
            - **{attempt['title']}** — Score: `{attempt['score']}%` ({attempt['timestamp'].strftime('%b %d, %I:%M %p')})  
              *Transcript:* "{attempt['transcript'][:120]}..."
            """)
