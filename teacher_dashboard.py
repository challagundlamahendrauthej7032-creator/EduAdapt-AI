"""
EduAdapt AI - Teacher Dashboard View
Provides deep pedagogical analytics, class concept heatmaps, at-risk student monitoring,
and cohort performance insights across Class 10 Physics sections.
"""

import pandas as pd
import streamlit as st
from config import CONCEPTS, CONCEPT_MAP
from data.student_data import STUDENT_ROSTER, get_class_summary_metrics
from components.ui_helpers import render_hero, render_status_pill
from components.charts import create_class_concept_heatmap, create_risk_distribution_chart, create_score_histogram


def render_teacher_dashboard():
    """Renders the comprehensive Teacher Analytics Dashboard."""
    render_hero(
        title="Educator & Faculty Portal 👨‍🏫",
        subtitle="Cohort-level diagnostics, concept difficulty analysis, at-risk learner tracking, and intervention planning.",
        tag="Teacher Analytics • Class 10 Physics"
    )

    # Section Filter Controls
    top_c1, top_c2 = st.columns([1, 2])
    with top_c1:
        section_choice = st.selectbox(
            "Select Section / Cohort:",
            options=["All Sections (10-A & 10-B)", "Section 10-A", "Section 10-B"],
            index=0
        )

    filter_val = "10-A" if "10-A" in section_choice and "All" not in section_choice else "10-B" if "10-B" in section_choice and "All" not in section_choice else "All"
    metrics = get_class_summary_metrics(filter_val)

    # Filtered Student List
    students = STUDENT_ROSTER
    if filter_val != "All":
        students = [s for s in students if s["section"] == filter_val]

    # Class Summary KPI Cards
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(
            label="👥 Total Enrolled Students",
            value=metrics.get("total_students", 30),
            delta="100% Diagnostic Participation"
        )
    with kpi2:
        st.metric(
            label="📊 Class Average Score",
            value=f"{metrics.get('avg_overall_score', 0)}%",
            delta=f"Diag Avg: {metrics.get('avg_diagnostic_score', 0)}/5"
        )
    with kpi3:
        high_risk_num = metrics.get("high_risk_count", 0)
        st.metric(
            label="⚠️ Students At Risk (<50%)",
            value=high_risk_num,
            delta="Needs Remedial Support" if high_risk_num > 0 else "None!",
            delta_color="inverse" if high_risk_num > 0 else "normal"
        )
    with kpi4:
        st.metric(
            label="🏫 Class Attendance Rate",
            value=f"{metrics.get('avg_attendance', 0)}%",
            delta="Average across term"
        )

    st.markdown("---")

    # Cohort Concept Analytics Row
    chart_col1, chart_col2 = st.columns([3, 2])

    with chart_col1:
        st.subheader("📈 Chapter Difficulty & Mastery Breakdown")
        heatmap = create_class_concept_heatmap(metrics.get("concept_averages", {}))
        st.altair_chart(heatmap, use_container_width=True)

        hardest_name = metrics.get("hardest_concept_name", "Electricity")
        hardest_avg = metrics.get("hardest_concept_avg", 50)
        st.warning(f"🚨 **Class Bottleneck Topic:** **{hardest_name}** has the lowest cohort mastery at **{hardest_avg}%**. Common stumbling block: combining series and parallel resistors.")

    with chart_col2:
        st.subheader("🎯 Student Performance Tiers")
        risk_chart = create_risk_distribution_chart(
            high_risk=metrics.get("high_risk_count", 0),
            moderate=metrics.get("moderate_count", 0),
            high_achievers=metrics.get("high_achiever_count", 0)
        )
        st.altair_chart(risk_chart, use_container_width=True)

    st.markdown("---")

    # Automated Pedagogical Recommendations for Teachers
    st.subheader("💡 AI Pedagogical Insights & Action Plan")
    rec_c1, rec_c2 = st.columns(2)
    
    with rec_c1:
        st.markdown(f"""
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-left: 5px solid #3b82f6; border-radius: 10px; padding: 1rem;">
            <b style="color: #1e40af; font-size: 0.95rem;">📌 Recommended Classroom Interventions:</b>
            <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem; color: #1e3a8a; font-size: 0.88rem; line-height: 1.6;">
                <li>Conduct a 20-minute live demonstration on <b>Ohm's Law numericals</b> and equivalent parallel resistances.</li>
                <li>Review the <b>Sign Conventions in Mirror & Lens Formulas</b> before next Monday's mock.</li>
                <li>Pair the <b>{metrics.get('high_risk_count', 0)} at-risk students</b> with high achievers for peer problem-solving.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with rec_c2:
        st.markdown(f"""
        <div style="background: #fdf4ff; border: 1px solid #f0abfc; border-left: 5px solid #c026d3; border-radius: 10px; padding: 1rem;">
            <b style="color: #86198f; font-size: 0.95rem;">🎙️ Voice Dictation Adoption Insight:</b>
            <p style="margin: 0.5rem 0 0 0; color: #701a75; font-size: 0.88rem; line-height: 1.5;">
                Students utilizing <b>Wispr Flow Voice Dictation</b> improved conceptual clarity scores by <b>+18%</b> on subjective questions like <i>Snell's Law</i> and <i>Fleming's Left Hand Rule</i>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Student Roster Table with Search & Filter
    st.subheader("📋 Student Performance Roster")

    f_col1, f_col2, f_col3 = st.columns([2, 1, 1])
    with f_col1:
        search_query = st.text_input("🔍 Search by Student Name or Roll No:", placeholder="e.g. Diya or STU102")
    with f_col2:
        risk_filter = st.selectbox("Filter by Risk Tier:", ["All Tiers", "High Risk (<50%)", "Moderate", "High Achiever"])
    with f_col3:
        sort_by = st.selectbox("Sort By:", ["Score (High to Low)", "Score (Low to High)", "Roll No", "Attendance"])

    # Apply search filter
    filtered = students
    if search_query:
        q_lower = search_query.lower()
        filtered = [s for s in filtered if q_lower in s["name"].lower() or q_lower in s["id"].lower() or str(s["roll_no"]) == search_query.strip()]

    # Apply risk filter
    if risk_filter == "High Risk (<50%)":
        filtered = [s for s in filtered if s["risk_category"] == "High Risk"]
    elif risk_filter == "Moderate":
        filtered = [s for s in filtered if s["risk_category"] == "Moderate"]
    elif risk_filter == "High Achiever":
        filtered = [s for s in filtered if s["risk_category"] == "High Achiever"]

    # Apply sorting
    if sort_by == "Score (High to Low)":
        filtered.sort(key=lambda x: x["overall_score"], reverse=True)
    elif sort_by == "Score (Low to High)":
        filtered.sort(key=lambda x: x["overall_score"])
    elif sort_by == "Roll No":
        filtered.sort(key=lambda x: (x["section"], x["roll_no"]))
    elif sort_by == "Attendance":
        filtered.sort(key=lambda x: x["attendance_pct"], reverse=True)

    # Convert to display table
    table_rows = []
    for s in filtered:
        weak_str = ", ".join([CONCEPT_MAP[c]["short_name"] for c in s["weak_concepts"] if c in CONCEPT_MAP]) or "None (Healthy)"
        table_rows.append({
            "ID": s["id"],
            "Name": s["name"],
            "Sec": s["section"],
            "Roll": s["roll_no"],
            "Diag": f"{s['diagnostic_score']}/5",
            "Score": f"{s['overall_score']}%",
            "Attendance": f"{s['attendance_pct']}%",
            "Weak Areas": weak_str,
            "Risk Tier": s["risk_category"]
        })

    df_roster = pd.DataFrame(table_rows)
    st.dataframe(df_roster, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Individual Student Deep Dive Drawer
    st.subheader("🔍 Individual Student Deep-Dive")
    student_names = [f"{s['name']} ({s['id']} - {s['section']})" for s in students]
    selected_student_str = st.selectbox("Select Student to inspect mastery profile:", options=student_names)

    selected_id = selected_student_str.split("(")[1].split(" -")[0]
    student_obj = next((s for s in students if s["id"] == selected_id), None)

    if student_obj:
        d_col1, d_col2 = st.columns([1, 2])
        with d_col1:
            st.markdown(f"""
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.2rem;">
                <div style="font-size: 1.3rem; font-weight: 700; color: #1e293b;">{student_obj['name']}</div>
                <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.6rem;">{student_obj['id']} • Section {student_obj['section']} • Roll #{student_obj['roll_no']}</div>
                <hr style="margin: 0.5rem 0;">
                <div><b>Overall Score:</b> <span style="font-size: 1.1rem; font-weight: bold; color: #3b82f6;">{student_obj['overall_score']}%</span></div>
                <div><b>Diagnostic:</b> {student_obj['diagnostic_score']} / 5</div>
                <div><b>Attendance:</b> {student_obj['attendance_pct']}%</div>
                <div><b>Practice Accuracy:</b> {student_obj['practice_accuracy_pct']}% ({student_obj['questions_attempted']} solved)</div>
                <div style="margin-top: 0.6rem;"><b>Status:</b> {render_status_pill(student_obj['risk_category'])}</div>
            </div>
            """, unsafe_allow_html=True)

        with d_col2:
            st.markdown(f"**Concept Breakdown for {student_obj['name']}:**")
            for c in CONCEPTS:
                cid = c["id"]
                val = student_obj["concept_mastery"].get(cid, 0)
                st.write(f"{c['icon']} **{c['short_name']}:** {val}%")
                st.progress(val / 100.0)

            st.markdown(f"""
            <div style="background: #f8fafc; border: 1px dashed #94a3b8; border-radius: 8px; padding: 0.8rem; margin-top: 0.8rem;">
                <b>👨‍🏫 Teacher Note & Recommendation:</b><br>
                {student_obj['teacher_notes']}
            </div>
            """, unsafe_allow_html=True)
