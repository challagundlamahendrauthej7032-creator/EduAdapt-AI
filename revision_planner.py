"""
EduAdapt AI - Revision Schedule & Spaced Repetition Planner
Provides a simple, science-backed revision schedule based on concept mastery
and the Ebbinghaus forgetting curve.
"""

from datetime import datetime
import streamlit as st
from config import CONCEPTS, CONCEPT_MAP, BOARD_EXAM_DATE
from components.ui_helpers import render_hero, render_status_pill


def render_revision_planner(learner_model):
    """Renders the Spaced Repetition Revision Schedule."""
    render_hero(
        title="Smart Revision Schedule 📅",
        subtitle="Spaced Repetition engine automatically plans your revision dates based on cognitive retention and concept mastery.",
        tag="Spaced Repetition • Class 10 Board Prep"
    )

    # Calculate summary metrics
    schedule = learner_model.revision_schedule
    due_today_count = sum(1 for item in schedule if "Today" in item.get("due_display", ""))
    avg_retention = sum(item.get("retention_level", 70) for item in schedule) / len(schedule) if schedule else 70

    # Summary Row
    r_col1, r_col2, r_col3, r_col4 = st.columns(4)
    with r_col1:
        st.metric(
            label="📌 Due for Revision Today",
            value=f"{due_today_count} Topics",
            delta="High Priority" if due_today_count > 0 else "All Caught Up!",
            delta_color="inverse" if due_today_count > 0 else "normal"
        )
    with r_col2:
        st.metric(
            label="🧠 Average Memory Retention",
            value=f"{int(avg_retention)}%",
            delta="+8% retention gain"
        )
    with r_col3:
        st.metric(
            label="⏳ Target Board Exam",
            value=BOARD_EXAM_DATE,
            delta="CBSE Class 10"
        )
    with r_col4:
        st.metric(
            label="🔥 Active Revision Streak",
            value=f"{learner_model.study_streak_days} Days",
            delta="Keep it going!"
        )

    st.markdown("---")

    # Spaced Repetition Theory Callout
    with st.expander("ℹ️ How the EduAdapt AI Spaced Repetition Engine Works", expanded=False):
        st.markdown("""
        **The Science of Spaced Repetition (Ebbinghaus Forgetting Curve):**
        - **Weak / Low Mastery Topics (< 55%):** Scheduled for immediate review (*Day 1 & Day 3*) to prevent memory decay.
        - **Developing Topics (55-79%):** Scheduled every *4 to 7 days* to consolidate working memory into long-term memory.
        - **Mastered Topics (≥ 80%):** Scheduled for maintenance review every *10 to 14 days*.
        - When you click **'Mark as Revised'**, your retention level increases and the next review interval expands automatically!
        """)

    st.subheader("🗓️ Active Revision Timeline")

    if not schedule:
        st.info("No revision tasks currently scheduled.")
        return

    # Loop through scheduled items
    for item in schedule:
        cid = item["concept_id"]
        c_meta = CONCEPT_MAP.get(cid, {})
        priority = item["priority"]
        retention = item["retention_level"]
        is_today = "Today" in item["due_display"]

        # Color and border class
        card_border = "#ef4444" if priority == "Critical" else "#f59e0b" if priority == "Moderate" else "#10b981"
        bg_tint = "#fef2f2" if is_today else "#ffffff"

        col_main, col_btn = st.columns([3, 1])

        with col_main:
            st.markdown(f"""
            <div style="background: {bg_tint}; border: 1px solid #e2e8f0; border-left: 6px solid {card_border}; border-radius: 12px; padding: 1.1rem 1.3rem; margin-bottom: 0.8rem; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                    <span style="font-size: 1.1rem; font-weight: 700; color: #1e293b;">
                        {item.get('icon', '📖')} {item['concept_name']}
                    </span>
                    <span style="font-size: 0.8rem; font-weight: 700; color: {card_border};">
                        ● {item['due_display']}
                    </span>
                </div>
                <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.6rem;">
                    <b>Recommended Study Mode:</b> {item['recommended_mode']}
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 0.8rem; font-weight: 600; color: #475569;">Retention Level: {retention}%</span>
                    <div style="flex-grow: 1; background: #e2e8f0; height: 8px; border-radius: 999px; overflow: hidden;">
                        <div style="width: {retention}%; background: {card_border}; height: 100%;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_btn:
            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            # Functional button to mark as revised
            if st.button("✅ Mark as Revised", key=f"rev_btn_{cid}", use_container_width=True):
                learner_model.mark_concept_revised(cid)
                st.toast(f"🎉 Revision logged for {c_meta.get('short_name', 'Concept')}! Retention boosted.", icon="🧠")
                st.rerun()

            if st.button("🎯 Practice Now", key=f"rev_prac_{cid}", use_container_width=True, type="secondary"):
                st.session_state["nav_selection"] = "Adaptive Practice"
                st.session_state["selected_practice_concept"] = cid
                st.rerun()

    st.markdown("---")

    # Quick revision checklist
    st.subheader("📋 Board Exam Formula Sheet Quick Access")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("**Light & Optics Formulas:**")
        st.code("Mirror: 1/f = 1/v + 1/u | Magnification: m = -v/u = h'/h\nLens: 1/f = 1/v - 1/u | Magnification: m = +v/u = h'/h\nPower: P = 1 / f(in meters) [Dioptres (D)]\nRefractive index: n = c / v = sin(i) / sin(r)", language="text")
    with col_f2:
        st.markdown("**Electricity & Magnetism Formulas:**")
        st.code("Ohm's Law: V = I · R\nSeries: R_s = R₁ + R₂ | Parallel: 1/R_p = 1/R₁ + 1/R₂\nJoule's Law: H = I² · R · t\nElectric Power: P = V · I = I²R = V²/R\nCommercial Energy: 1 kWh = 3.6 × 10⁶ Joules", language="text")
