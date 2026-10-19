"""
UI Components & Corporate Styling for Sugar Cosmetics Analytics Dashboard
Includes:
- Sugar Cosmetics brand theme (Magenta/Berry/Dark Charcoal)
- 'About this Section' Top Containers (Mandatory User Requirement)
- 'What this Graph is Telling' Bottom Takeaway Cards (Mandatory User Requirement)
- Professional KPI Cards & Spacing Utilities
"""

import streamlit as st

def apply_custom_css():
    """Inject corporate luxury styling with Sugar Cosmetics signature palette."""
    custom_css = """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main background */
    .stApp {
        background-color: #0b0d13;
        color: #f1f3f9;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #10121a 0%, #151824 100%);
        border-right: 1px solid rgba(255, 0, 127, 0.15);
    }
    
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.8rem;
    }

    /* Custom Title & Header styles */
    .brand-header-box {
        background: linear-gradient(135deg, rgba(255, 0, 127, 0.12) 0%, rgba(121, 40, 202, 0.08) 50%, rgba(11, 13, 19, 0.9) 100%);
        border: 1px solid rgba(255, 0, 127, 0.35);
        border-radius: 16px;
        padding: 24px 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
        backdrop-filter: blur(10px);
    }

    .brand-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.1rem;
        font-weight: 700;
        background: linear-gradient(90deg, #FFFFFF 0%, #FF64B0 60%, #FF007F 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }

    .brand-subtitle {
        color: #A0AEC0;
        font-size: 0.95rem;
        font-weight: 400;
        margin: 0;
    }

    .brand-badge {
        display: inline-block;
        background: rgba(255, 0, 127, 0.18);
        border: 1px solid #FF007F;
        color: #FF66B2;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 10px;
    }

    /* ABOUT SECTION (Mandatory User Requirement for top of each page) */
    .about-card {
        background: linear-gradient(135deg, #131722 0%, #171b29 100%);
        border-left: 5px solid #FF007F;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 28px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }

    .about-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 8px;
    }

    .about-tag {
        background: rgba(255, 0, 127, 0.15);
        color: #FF52A2;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border: 1px solid rgba(255, 0, 127, 0.3);
    }

    .about-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #FFFFFF;
        margin: 0;
    }

    .about-desc {
        color: #B5BFD0;
        font-size: 0.92rem;
        line-height: 1.6;
        margin-bottom: 12px;
    }

    .about-meta-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 12px;
        margin-top: 12px;
        padding-top: 12px;
        border-top: 1px solid rgba(255, 255, 255, 0.07);
    }

    .about-meta-item {
        font-size: 0.82rem;
        color: #8C9BAE;
    }

    .about-meta-item strong {
        color: #E2E8F0;
    }

    /* KPI METRIC CARDS */
    .kpi-card {
        background: linear-gradient(135deg, #141724 0%, #191E2E 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        position: relative;
        overflow: hidden;
    }

    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 0, 127, 0.4);
        box-shadow: 0 8px 25px rgba(255, 0, 127, 0.15);
    }

    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #FF007F, #9A30AE);
    }

    .kpi-label {
        font-size: 0.82rem;
        color: #8C9BAE;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-bottom: 6px;
    }

    .kpi-value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.75rem;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.2;
        margin-bottom: 4px;
    }

    .kpi-subtext {
        font-size: 0.78rem;
        color: #A0AEC0;
    }

    .kpi-badge-positive {
        color: #10B981;
        font-weight: 600;
        font-size: 0.78rem;
    }

    /* GRAPH TAKEAWAY CARD (Mandatory User Requirement for below each graph) */
    .takeaway-card {
        background: #11141E;
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-left: 4px solid #38BDF8;
        border-radius: 10px;
        padding: 16px 20px;
        margin-top: 10px;
        margin-bottom: 28px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
    }

    .takeaway-card.pink-accent {
        border-left-color: #FF007F;
    }

    .takeaway-card.gold-accent {
        border-left-color: #F59E0B;
    }

    .takeaway-card.green-accent {
        border-left-color: #10B981;
    }

    .takeaway-title {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.95rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 10px;
        letter-spacing: 0.2px;
    }

    .takeaway-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 8px;
        font-size: 0.87rem;
        color: #CBD5E1;
        line-height: 1.55;
    }

    .takeaway-pill {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 0.72rem;
        margin-right: 6px;
        text-transform: uppercase;
    }

    .pill-obs { background: rgba(56, 189, 248, 0.2); color: #7DD3FC; }
    .pill-biz { background: rgba(245, 158, 11, 0.2); color: #FCD34D; }
    .pill-act { background: rgba(255, 0, 127, 0.2); color: #FF80BF; }

    /* Streamlit widgets overrides */
    .stSelectbox, .stMultiSelect, .stSlider, .stDateInput {
        color: #FFFFFF !important;
    }

    /* Metric container styling */
    div[data-testid="stMetricValue"] {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #FFFFFF !important;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        height: 44px;
        white-space: pre-wrap;
        border-radius: 8px 8px 0px 0px;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 18px;
        padding-right: 18px;
        font-weight: 600;
        color: #94A3B8;
        background-color: transparent;
        border: none;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(255, 0, 127, 0.12) !important;
        color: #FF3399 !important;
        border-bottom: 2px solid #FF007F !important;
    }

    /* Clean spacing */
    .section-divider {
        margin-top: 30px;
        margin-bottom: 25px;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def render_brand_header(title="Instagram Performance Analytics", subtitle="Sugar Cosmetics Brand Growth & Intelligence Portal"):
    """Render signature Sugar Cosmetics executive header."""
    html = f"""
    <div class="brand-header-box">
        <span class="brand-badge">SUGAR COSMETICS • BUSINESS INTELLIGENCE</span>
        <div class="brand-title">{title}</div>
        <p class="brand-subtitle">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_about_section(section_name, description, key_questions=None, metrics_tracked=None):
    """
    Mandatory requirement: Render top 'About Section' for each page explaining
    page contents, scope, business purpose, and metrics analyzed.
    """
    questions_html = ""
    if key_questions:
        items = "".join([f"<li>{q}</li>" for q in key_questions])
        questions_html = f"""
        <div class="about-meta-item">
            <strong>🎯 Key Business Questions Addressed:</strong>
            <ul style="margin: 4px 0 0 18px; padding: 0;">{items}</ul>
        </div>
        """

    metrics_html = ""
    if metrics_tracked:
        items = " • ".join(metrics_tracked)
        metrics_html = f"""
        <div class="about-meta-item">
            <strong>📊 Primary Metrics Analyzed:</strong> <span style="color:#F1F5F9;">{items}</span>
        </div>
        """

    html = f"""
    <div class="about-card">
        <div class="about-header">
            <span class="about-tag">ℹ️ Page Guide & Purpose</span>
            <h3 class="about-title">{section_name}</h3>
        </div>
        <p class="about-desc">{description}</p>
        <div class="about-meta-grid">
            {metrics_html}
            {questions_html}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_chart_takeaway(chart_title, observation, business_meaning, action_item, accent="pink"):
    """
    Mandatory requirement: Render informative card below each graph explaining
    what the chart demonstrates, business insights, and marketing recommendation.
    """
    accent_class = {
        "pink": "pink-accent",
        "gold": "gold-accent",
        "green": "green-accent",
        "blue": ""
    }.get(accent, "pink-accent")

    html = f"""
    <div class="takeaway-card {accent_class}">
        <div class="takeaway-title">
            <span>💡 Chart Insight & Strategic Takeaway: <strong>{chart_title}</strong></span>
        </div>
        <div class="takeaway-grid">
            <div>
                <span class="takeaway-pill pill-obs">Data Finding</span>
                {observation}
            </div>
            <div>
                <span class="takeaway-pill pill-biz">Business Impact</span>
                {business_meaning}
            </div>
            <div>
                <span class="takeaway-pill pill-act">Action Recommendation</span>
                {action_item}
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_kpi_card(label, value, subtext="", badge="", positive=True):
    """Render polished corporate metric card."""
    badge_html = f'<div class="kpi-badge-positive">{badge}</div>' if badge else ''
    html = f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-subtext">{subtext}</div>
        {badge_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
