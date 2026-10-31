"""
EduAdapt AI - Interactive Charts Component (Altair & Streamlit Native)
Visualizes student concept mastery, score distributions, and class heatmaps.
"""

import pandas as pd
import altair as alt
import streamlit as st
from config import CONCEPTS, CONCEPT_MAP, MASTERY_THRESHOLDS


def create_mastery_bar_chart(concept_mastery: dict):
    """
    Horizontal bar chart showing mastery percentage for each Physics concept,
    color-coded by mastery status with an 80% target line.
    """
    rows = []
    for c in CONCEPTS:
        cid = c["id"]
        val = concept_mastery.get(cid, 50.0)
        
        if val >= MASTERY_THRESHOLDS["mastered"]:
            status = "Mastered (≥80%)"
            color = "#10b981"  # Emerald
        elif val >= MASTERY_THRESHOLDS["developing"]:
            status = "Developing (55-79%)"
            color = "#f59e0b"  # Amber
        else:
            status = "Needs Focus (<55%)"
            color = "#ef4444"  # Red

        rows.append({
            "Concept": f"{c['icon']} {c['short_name']}",
            "Full Name": c["name"],
            "Mastery": val,
            "Status": status,
            "Color": color
        })

    df = pd.DataFrame(rows)

    # Sort descending by mastery
    df = df.sort_values(by="Mastery", ascending=False)

    base = alt.Chart(df).encode(
        y=alt.Y("Concept:N", sort="-x", title="", axis=alt.Axis(labelFontSize=13, labelFontWeight="bold")),
        x=alt.X("Mastery:Q", scale=alt.Scale(domain=[0, 100]), title="Mastery Level (%)", axis=alt.Axis(grid=True, labelFontSize=11)),
        tooltip=[
            alt.Tooltip("Full Name:N", title="Concept"),
            alt.Tooltip("Mastery:Q", title="Mastery %", format=".1f"),
            alt.Tooltip("Status:N", title="Status")
        ]
    )

    bars = base.mark_bar(cornerRadiusTopRight=6, cornerRadiusBottomRight=6, height=24).encode(
        color=alt.Color(
            "Status:N",
            scale=alt.Scale(
                domain=["Needs Focus (<55%)", "Developing (55-79%)", "Mastered (≥80%)"],
                range=["#ef4444", "#f59e0b", "#10b981"]
            ),
            legend=alt.Legend(title="Mastery Tier", orient="top")
        )
    )

    text = base.mark_text(
        align="left",
        baseline="middle",
        dx=8,
        fontSize=12,
        fontWeight="bold"
    ).encode(
        text=alt.Text("Mastery:Q", format=".0f"),
        color=alt.value("#334155")
    )

    # 80% Board Target Rule
    target_rule = alt.Chart(pd.DataFrame({"Target": [80]})).mark_rule(
        strokeDash=[4, 4],
        color="#047857",
        size=2
    ).encode(
        x="Target:Q"
    )

    chart = (bars + text + target_rule).properties(
        height=260,
        title=alt.TitleParams(
            text="Physics Concept Mastery Breakdown",
            subtitle="Target: ≥80% for Board Exam A1 Grade",
            fontSize=15,
            fontWeight="bold",
            subtitleFontSize=11,
            subtitleColor="#64748b"
        )
    ).configure_view(
        strokeWidth=0
    )

    return chart


def create_class_concept_heatmap(concept_averages: dict):
    """
    Bar chart showing Class 10 average performance across all Physics topics.
    """
    rows = []
    for c in CONCEPTS:
        cid = c["id"]
        avg_val = concept_averages.get(cid, 60.0)
        
        if avg_val >= 75:
            tier = "High Strength"
        elif avg_val >= 55:
            tier = "Moderate"
        else:
            tier = "At-Risk Topic"

        rows.append({
            "Concept": f"{c['icon']} {c['short_name']}",
            "Class Average": avg_val,
            "Tier": tier
        })

    df = pd.DataFrame(rows).sort_values(by="Class Average", ascending=True)

    chart = alt.Chart(df).mark_bar(cornerRadiusTopRight=5, cornerRadiusBottomRight=5, height=22).encode(
        y=alt.Y("Concept:N", sort="-x", title="", axis=alt.Axis(labelFontSize=12)),
        x=alt.X("Class Average:Q", scale=alt.Scale(domain=[0, 100]), title="Class Average Mastery (%)"),
        color=alt.Color(
            "Tier:N",
            scale=alt.Scale(
                domain=["At-Risk Topic", "Moderate", "High Strength"],
                range=["#ef4444", "#f59e0b", "#10b981"]
            ),
            legend=alt.Legend(title="Concept Health", orient="top")
        ),
        tooltip=[
            alt.Tooltip("Concept:N"),
            alt.Tooltip("Class Average:Q", format=".1f", title="Avg Score %"),
            alt.Tooltip("Tier:N")
        ]
    ).properties(
        height=240,
        title="Class Mastery by Physics Chapter"
    )

    return chart


def create_risk_distribution_chart(high_risk: int, moderate: int, high_achievers: int):
    """
    Donut/Pie style bar breakdown of student risk categories.
    """
    df = pd.DataFrame([
        {"Category": "High Risk (<50%)", "Students": high_risk, "Color": "#ef4444"},
        {"Category": "Moderate (50-74%)", "Students": moderate, "Color": "#f59e0b"},
        {"Category": "High Achiever (≥75%)", "Students": high_achievers, "Color": "#10b981"}
    ])

    chart = alt.Chart(df).mark_arc(innerRadius=45, stroke="#ffffff", strokeWidth=2).encode(
        theta=alt.Theta("Students:Q", title="Students"),
        color=alt.Color(
            "Category:N",
            scale=alt.Scale(
                domain=["High Risk (<50%)", "Moderate (50-74%)", "High Achiever (≥75%)"],
                range=["#ef4444", "#f59e0b", "#10b981"]
            ),
            legend=alt.Legend(title="Student Category", orient="bottom")
        ),
        tooltip=[
            alt.Tooltip("Category:N"),
            alt.Tooltip("Students:Q", title="Student Count")
        ]
    ).properties(
        height=220,
        title="Student Risk Tier Distribution"
    )

    return chart


def create_score_histogram(roster_data: list):
    """Histogram showing distribution of overall scores across the class."""
    scores = [s["overall_score"] for s in roster_data]
    df = pd.DataFrame({"Score": scores})

    chart = alt.Chart(df).mark_bar(color="#6366f1", cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
        x=alt.X("Score:Q", bin=alt.Bin(maxbins=8), title="Overall Score (%)"),
        y=alt.Y("count()", title="Number of Students"),
        tooltip=[
            alt.Tooltip("count()", title="Students in Range")
        ]
    ).properties(
        height=200,
        title="Score Spread Distribution"
    )

    return chart
