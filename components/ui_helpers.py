"""
UI Helpers and Custom Styling for EduAdapt AI
Provides consistent CSS theming, badges, alert cards, and layout wrappers.
"""

import streamlit as st


def apply_custom_css():
    """Inject polished, modern CSS into the Streamlit application."""
    custom_css = """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main container max width & spacing */
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3.5rem;
        max-width: 1200px;
    }

    /* Hero Gradient Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%);
        color: white;
        padding: 1.8rem 2.2rem;
        border-radius: 18px;
        box-shadow: 0 10px 25px -5px rgba(49, 46, 129, 0.3);
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .hero-banner h1 {
        font-size: 2.1rem;
        font-weight: 800;
        margin: 0 0 0.4rem 0;
        letter-spacing: -0.02em;
        color: #ffffff;
    }
    .hero-banner p {
        font-size: 1.05rem;
        opacity: 0.9;
        margin: 0;
        line-height: 1.5;
        color: #e0e7ff;
    }

    /* Feature Metric Card */
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.3rem 1.4rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.08);
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.35rem;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .metric-caption {
        font-size: 0.82rem;
        color: #64748b;
    }

    /* Status Pills / Badges */
    .badge {
        display: inline-block;
        padding: 0.28rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        text-transform: uppercase;
    }
    .badge-mastered {
        background-color: #d1fae5;
        color: #065f46;
        border: 1px solid #a7f3d0;
    }
    .badge-developing {
        background-color: #fef3c7;
        color: #92400e;
        border: 1px solid #fde68a;
    }
    .badge-weak {
        background-color: #fee2e2;
        color: #991b1b;
        border: 1px solid #fecaca;
    }

    /* Question Container */
    .question-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #4f46e5;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .question-tag {
        display: inline-block;
        background: #eef2ff;
        color: #4338ca;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    /* Feedback Cards */
    .feedback-box-correct {
        background: #ecfdf5;
        border: 1px solid #6ee7b7;
        border-left: 6px solid #10b981;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin: 1rem 0;
    }
    .feedback-box-incorrect {
        background: #fff1f2;
        border: 1px solid #fca5a5;
        border-left: 6px solid #ef4444;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin: 1rem 0;
    }

    /* Formula Pill */
    .formula-callout {
        background: #f8fafc;
        border: 1px dashed #94a3b8;
        border-radius: 8px;
        padding: 0.6rem 0.9rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #334155;
        margin: 0.5rem 0;
    }

    /* Wispr Flow Voice Widget Style */
    .wispr-header {
        background: linear-gradient(135deg, #09090b 0%, #18181b 100%);
        color: #fafafa;
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #27272a;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .wispr-pill {
        background: #27272a;
        color: #a1a1aa;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .wispr-badge {
        background: #8b5cf6;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
    }

    /* Schedule Timeline Card */
    .schedule-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .schedule-card.priority-critical {
        border-left: 5px solid #ef4444;
    }
    .schedule-card.priority-moderate {
        border-left: 5px solid #f59e0b;
    }
    .schedule-card.priority-low {
        border-left: 5px solid #10b981;
    }

    /* Sidebar enhancement */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    section[data-testid="stSidebar"] * {
        color: #e2e8f0;
    }
    section[data-testid="stSidebar"] .stRadio > label {
        color: #94a3b8 !important;
        font-weight: 600;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def render_hero(title: str, subtitle: str, tag: str = "Class 10 Physics"):
    """Render attractive hero header banner."""
    html = f"""
    <div class="hero-banner">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
            <div>
                <span style="background: rgba(255,255,255,0.18); padding: 0.2rem 0.7rem; border-radius: 9999px; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.04em;">{tag}</span>
                <h1 style="margin-top: 0.5rem;">{title}</h1>
                <p>{subtitle}</p>
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_metric_card(title: str, value: str, caption: str = "", delta: str = None, delta_color: str = "#10b981"):
    """Render a clean dashboard metric card."""
    delta_html = ""
    if delta:
        delta_html = f"<div style='font-size: 0.8rem; font-weight: 600; color: {delta_color}; margin-top: 0.2rem;'>{delta}</div>"

    html = f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
        <div class="metric-caption">{caption}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_status_pill(status: str) -> str:
    """Return HTML for a status badge."""
    cls_map = {
        "Mastered": "badge-mastered",
        "Developing": "badge-developing",
        "Needs Focus": "badge-weak",
        "Critical": "badge-weak",
        "Moderate": "badge-developing",
        "Low": "badge-mastered"
    }
    badge_cls = cls_map.get(status, "badge-developing")
    return f'<span class="badge {badge_cls}">{status}</span>'


def render_feedback_card(is_correct: bool, explanation: str, formula: str = None, why_wrong: str = None, board_tip: str = None):
    """Render a comprehensive, useful feedback card after answering a question."""
    if is_correct:
        header = "🎉 <b>Correct Answer! Excellent conceptual grasp.</b>"
        box_class = "feedback-box-correct"
    else:
        header = "💡 <b>Incorrect — Here is the step-by-step breakdown:</b>"
        box_class = "feedback-box-incorrect"

    formula_html = ""
    if formula:
        formula_html = f"""
        <div style="margin-top: 0.6rem;">
            <b style="font-size: 0.85rem; color: #1e293b;">📐 Core Formula:</b>
            <div class="formula-callout">{formula}</div>
        </div>
        """

    trap_html = ""
    if why_wrong and not is_correct:
        trap_html = f"""
        <div style="margin-top: 0.6rem; padding: 0.6rem 0.8rem; background: #ffe4e6; border-radius: 8px; font-size: 0.85rem; color: #881337;">
            <b>⚠️ Common Exam Misconception:</b> {why_wrong}
        </div>
        """

    tip_html = ""
    if board_tip:
        tip_html = f"""
        <div style="margin-top: 0.6rem; padding: 0.6rem 0.8rem; background: #eff6ff; border-radius: 8px; font-size: 0.85rem; color: #1e40af;">
            <b>🎯 Class 10 Board Exam Tip:</b> {board_tip}
        </div>
        """

    html = f"""
    <div class="{box_class}">
        <div style="font-size: 1.05rem; margin-bottom: 0.6rem;">{header}</div>
        <div style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            {explanation.replace(chr(10), '<br>')}
        </div>
        {formula_html}
        {trap_html}
        {tip_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
