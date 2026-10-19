"""
Sugar Cosmetics - Instagram Performance Analytics Dashboard
Enterprise-Grade Social Media Intelligence & Growth Engine

Built with Streamlit & Plotly
Replaces Tableau / Power BI with interactive web analytics
"""

import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Sugar Cosmetics | Instagram Analytics BI",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Internal modules
from src.components import (
    apply_custom_css,
    render_brand_header,
    render_about_section,
    render_chart_takeaway,
    render_kpi_card
)
from src.data_loader import load_data, apply_filters, compute_executive_kpis
from src.charts import (
    chart_monthly_posting_trend,
    chart_top_posts_by_likes,
    chart_top_posts_by_engagement_rate,
    chart_post_type_comparison,
    chart_day_of_week_analysis,
    chart_engagement_funnel,
    chart_hashtag_performance,
    chart_campaign_type_distribution,
    chart_emotion_and_source_sunburst
)

# Apply corporate branding & CSS
apply_custom_css()

# Load dataset
try:
    df_raw = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# ==========================================
# SIDEBAR FILTERS & BRAND NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <span style="font-size: 2.2rem;">💄</span>
        <div style="font-size: 1.4rem; font-weight: 800; color: #FFFFFF; letter-spacing: -0.5px;">SUGAR</div>
        <div style="font-size: 0.75rem; color: #FF007F; font-weight: 700; letter-spacing: 2px;">COSMETICS</div>
        <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Social Media Business Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧭 Dashboard Navigation")
    pages = [
        "🏢 1. Executive Summary & KPIs",
        "📈 2. Monthly Posting Trends",
        "🏆 3. Top Content & Hidden Gems",
        "🎨 4. Post Format Benchmark",
        "📅 5. Day-of-Week Optimization",
        "🌪️ 6. Audience Engagement Funnel",
        "🏷️ 7. Hashtag & Campaign Strategy",
        "🎯 8. Strategic Recommendations",
        "🔍 9. Interactive Data Explorer"
    ]
    selected_page = st.radio("Select View:", pages, index=0)

    st.markdown("---")
    st.markdown("### 🎛️ Global Data Filters")

    # Date Range Filter
    min_date = df_raw['Post Date'].min().date()
    max_date = df_raw['Post Date'].max().date()
    date_filter = st.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # Post Type Multi-select
    all_post_types = sorted(df_raw['Post Type'].unique().tolist())
    selected_post_types = st.multiselect("Post Format", all_post_types, default=all_post_types)

    # Campaign Type Multi-select
    all_campaigns = sorted(df_raw['Campaign Type'].unique().tolist())
    selected_campaigns = st.multiselect("Campaign Type", all_campaigns, default=all_campaigns)

    # Engagement Source Multi-select
    all_sources = sorted(df_raw['Engagement Source'].unique().tolist())
    selected_sources = st.multiselect("Engagement Source", all_sources, default=all_sources)

    # Hashtags Filter
    hashtag_options = ["All Hashtags", "#SugarCosmetics", "#BoldLooks", "#CrueltyFree", "#MakeupGoals", "#VeganBeauty"]
    selected_hashtag = st.selectbox("Filter by Primary Tag", hashtag_options, index=0)

    # Audience Emotion Filter
    all_emotions = sorted(df_raw['Audience Emotion'].unique().tolist())
    selected_emotions = st.multiselect("Audience Emotion", all_emotions, default=all_emotions)

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.72rem; color: #64748B; text-align: center;">
        Dataset: 50,000 Verified Posts<br>
        Sugar Cosmetics Brand Analytics v2.5
    </div>
    """, unsafe_allow_html=True)

# Apply global interactive filters
filtered_df = apply_filters(
    df_raw,
    date_range=date_filter,
    post_types=selected_post_types,
    campaign_types=selected_campaigns,
    sources=selected_sources,
    emotions=selected_emotions,
    selected_hashtag=selected_hashtag
)

# Compute executive KPIs on filtered slice
kpis = compute_executive_kpis(filtered_df)

# ==========================================
# PAGE ROUTING & CONTENT
# ==========================================

# ------------------------------------------
# PAGE 1: EXECUTIVE SUMMARY & KPIS (Task 1)
# ------------------------------------------
if selected_page.startswith("🏢 1."):
    render_brand_header(
        title="Brand Instagram Performance Summary",
        subtitle="High-level executive scorecards, overall reach, and engagement health for Sugar Cosmetics"
    )

    # Mandatory About Section at top
    render_about_section(
        section_name="Overview KPIs & Brand Account Health",
        description="This executive dashboard sheet answers the primary question: <b>'How is the overall Sugar Cosmetics account performing?'</b> It provides a comprehensive macro-level aggregation of total visibility (Impressions and Reach), community engagement (Likes, Comments, Shares, Saves), and customer acquisition metrics (Profile Visits, Follow Conversion Rate). Use this page to evaluate quarterly brand momentum, campaign velocity, and overall return on organic and paid content investments.",
        key_questions=[
            "What is our cumulative brand visibility and community interaction count?",
            "What is our aggregate Engagement Rate relative to reach across all active campaigns?",
            "How effectively is top-of-funnel reach converting into profile visits and new followers?"
        ],
        metrics_tracked=[
            "Total Posts", "Total Reach", "Total Impressions", "Total Likes", 
            "Total Comments", "Total Shares & Saves", "Avg Engagement Rate (%)", "Follow Conversion Rate (%)"
        ]
    )

    # Executive KPI Cards Grid
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Posts Published", f"{kpis['total_posts']:,}", "Active catalog across all channels", "100% Monitored")
    with col2:
        render_kpi_card("Total Account Reach", f"{kpis['total_reach'] / 1e6:.2f}M", f"{kpis['avg_reach']:,.0f} avg reach per post", "Brand Visibility")
    with col3:
        render_kpi_card("Total Impressions", f"{kpis['total_impressions'] / 1e6:.2f}M", "Total content exposure count", "High Frequency")
    with col4:
        render_kpi_card("Avg Engagement Rate", f"{kpis['avg_engagement_rate']:.2f}%", "Interactions relative to unique reach", "Target > 15%", positive=True)

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        render_kpi_card("Total Likes", f"{kpis['total_likes'] / 1e6:.2f}M", "Direct audience appreciation", "Primary Volume")
    with col6:
        render_kpi_card("Total Comments", f"{kpis['total_comments'] / 1e6:.2f}M", "Active conversation & sentiment", "Community Dialogue")
    with col7:
        render_kpi_card("Total Saves & Shares", f"{(kpis['total_saves'] + kpis['total_shares']) / 1e6:.2f}M", f"{kpis['total_saves']:,} saves • {kpis['total_shares']:,} shares", "High-Value Actions")
    with col8:
        render_kpi_card("Follow Conversion Rate", f"{kpis['conversion_rate']:.2f}%", f"{kpis['total_follows'] / 1e6:.2f}M followers gained", "Growth Engine")

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # Interaction Distribution & Source Breakdown
    st.subheader("📊 Community Engagement Composition & Distribution")
    c_left, c_right = st.columns([1.2, 1])

    with c_left:
        # Breakdown of interactions
        interaction_df = pd.DataFrame({
            'Interaction Type': ['Likes', 'Comments', 'Saves (Evergreen)', 'Shares (Virality)'],
            'Count': [kpis['total_likes'], kpis['total_comments'], kpis['total_saves'], kpis['total_shares']]
        })
        import plotly.express as px
        fig_pie = px.pie(
            interaction_df,
            names='Interaction Type',
            values='Count',
            color='Interaction Type',
            color_discrete_map={
                'Likes': '#FF007F',
                'Comments': '#9D4EDD',
                'Saves (Evergreen)': '#00E5FF',
                'Shares (Virality)': '#FFB703'
            },
            hole=0.45,
            title="<b>Total Community Interaction Distribution</b>"
        )
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#CBD5E1"),
            legend=dict(orientation="h", y=-0.1)
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        render_chart_takeaway(
            chart_title="Interaction Distribution",
            observation=f"Likes constitute the largest interaction volume ({kpis['total_likes']/max(kpis['total_interactions'], 1):.1%}), while high-intent saves ({kpis['total_saves']:,}) and shares ({kpis['total_shares']:,}) represent {((kpis['total_saves'] + kpis['total_shares'])/max(kpis['total_interactions'], 1)):.1%} of all touchpoints.",
            business_meaning="While likes provide social proof, Instagram's algorithm heavily favors saves and shares for discovery page recommendation. The existing volume shows strong base affinity but opportunities in saveable tutorial content.",
            action_item="Introduce explicit save-call-to-actions ('Save this look for later') in captions to shift more passive likes into high-algorithmic-weight saves.",
            accent="pink"
        )

    with c_right:
        # Engagement Source Breakdown
        src_df = filtered_df.groupby('Engagement Source').agg(
            Total_Reach=('Reach', 'sum'),
            Avg_ER=('Engagement_Rate', 'mean')
        ).reset_index()

        fig_src = px.bar(
            src_df,
            x='Engagement Source',
            y='Total_Reach',
            color='Avg_ER',
            color_continuous_scale=[[0, '#2D0A31'], [0.5, '#7928CA'], [1, '#FF007F']],
            title="<b>Reach & Engagement Rate by Channel Source</b>",
            text=src_df['Total_Reach'].apply(lambda x: f"{x/1e6:.1f}M")
        )
        fig_src.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(19, 23, 34, 0.6)",
            font=dict(color="#CBD5E1"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.07)")
        )
        st.plotly_chart(fig_src, use_container_width=True)

        render_chart_takeaway(
            chart_title="Engagement Source Efficiency",
            observation="Organic, Collabs, and Influencer posts demonstrate well-distributed reach with average engagement remaining robust above 18% across channels.",
            business_meaning="Paid and Collab channels successfully amplify brand awareness without diluting authentic engagement quality.",
            action_item="Scale influencer and co-creation campaigns as primary awareness drivers while leveraging organic posts for community loyalty.",
            accent="gold"
        )

# ------------------------------------------
# PAGE 2: MONTHLY POSTING TRENDS (Task 2)
# ------------------------------------------
elif selected_page.startswith("📈 2."):
    render_brand_header(
        title="Monthly Posting Trend & Consistency Analysis",
        subtitle="Tracking publishing frequency, volume trajectory, and engagement evolution over time"
    )

    render_about_section(
        section_name="Posting Frequency & Longitudinal Performance",
        description="This section addresses <b>Task 2: Monthly Posting Trend</b>. Regularity and posting consistency are crucial determinants of Instagram algorithm favoritism and audience retention. This analysis converts post timestamps into Month-Year formats to uncover seasonality, publishing cadence stability, and whether surges in content output correlate with higher or diminished audience engagement rates.",
        key_questions=[
            "How consistent is Sugar Cosmetics' posting schedule across months?",
            "Does increasing publishing volume lead to audience fatigue or higher cumulative reach?",
            "Which months generated peak engagement rates, and what seasonal drivers caused them?"
        ],
        metrics_tracked=[
            "Monthly Post Count", "Monthly Cumulative Reach", "Monthly Average Engagement Rate (%)", "Interactions Trajectory"
        ]
    )

    # Monthly dual-axis chart
    fig_trend = chart_monthly_posting_trend(filtered_df)
    st.plotly_chart(fig_trend, use_container_width=True)

    render_chart_takeaway(
        chart_title="Monthly Posting Cadence vs Engagement Rate",
        observation="Monthly publishing volume shows healthy, disciplined consistency (~4,000 to 4,200 posts per month across channels), with engagement rate maintaining an impressive equilibrium between 18.2% and 18.8%.",
        business_meaning="Sugar Cosmetics avoids common 'burnout' dips, sustaining high brand recall through uninterrupted content delivery throughout festive, bridal, and summer beauty seasons.",
        action_item="Maintain the ~130 daily cross-format content cadence, while optimizing the monthly distribution of high-effort tutorial reels versus lightweight stories.",
        accent="blue"
    )

    # Secondary view: Monthly Reach & Impressions Volume
    st.subheader("📈 Monthly Reach & Impression Growth Trajectory")
    monthly_agg = filtered_df.groupby('Year_Month').agg(
        Total_Impressions=('Impressions', 'sum'),
        Total_Reach=('Reach', 'sum'),
        Total_Follows=('Follows', 'sum')
    ).reset_index().sort_values('Year_Month')

    import plotly.graph_objects as go
    fig_reach = go.Figure()
    fig_reach.add_trace(go.Scatter(
        x=monthly_agg['Year_Month'],
        y=monthly_agg['Total_Impressions'] / 1e6,
        name="Impressions (Millions)",
        mode="lines+markers",
        line=dict(color="#FF007F", width=3),
        fill="tozeroy",
        fillcolor="rgba(255, 0, 127, 0.1)"
    ))
    fig_reach.add_trace(go.Scatter(
        x=monthly_agg['Year_Month'],
        y=monthly_agg['Total_Reach'] / 1e6,
        name="Unique Reach (Millions)",
        mode="lines+markers",
        line=dict(color="#00E5FF", width=2.5)
    ))
    fig_reach.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(19, 23, 34, 0.6)",
        font=dict(color="#CBD5E1"),
        yaxis=dict(title="Millions", gridcolor="rgba(255,255,255,0.07)"),
        title="<b>Monthly Gross Impressions vs Unique Reach Growth</b>",
        hovermode="x unified"
    )
    st.plotly_chart(fig_reach, use_container_width=True)

    render_chart_takeaway(
        chart_title="Reach vs Impressions Ratio",
        observation="Gross Impressions consistently exceed Unique Reach by 1.29x, indicating strong repeat exposure where individual users view Sugar Cosmetics content multiple times per billing cycle.",
        business_meaning="High frequency per user builds deeper brand recall, critical for cosmetic product purchases which usually require 3-5 impressions before conversion.",
        action_item="Retarget highly engaged users who view multiple times with specific product discount codes and limited-edition product links.",
        accent="green"
    )

# ------------------------------------------
# PAGE 3: TOP CONTENT & HIDDEN GEMS (Tasks 3 & 4)
# ------------------------------------------
elif selected_page.startswith("🏆 3."):
    render_brand_header(
        title="Top Performing Content & Hidden Gems",
        subtitle="Identifying posts with maximum absolute likes and highest relative engagement rates"
    )

    render_about_section(
        section_name="Content Performance Extremes: Viral Hits vs. Hidden Gems",
        description="This section delivers <b>Task 3: Top 10 Posts by Likes</b> and <b>Task 4: Top 10 Posts by Engagement Rate</b>. In digital marketing, absolute likes identify high-reach mainstream hits, while engagement rate reveals 'hidden gems'—posts that may have reached a niche audience but elicited passionate interaction relative to their visibility. Comparing both dimensions enables the content team to double down on winning creative hooks.",
        key_questions=[
            "Which specific posts generated the highest absolute like counts?",
            "Which hidden gem posts achieved superlative engagement rates relative to their audience size?",
            "What commonalities exist in hashtags, formats, and emotions among top performers?"
        ],
        metrics_tracked=[
            "Likes Ranking", "Engagement Rate Ranking", "Reach", "Comments", "Saves", "Content Formats"
        ]
    )

    tab_likes, tab_er = st.tabs(["🔥 Top Posts by Likes (Task 3)", "💎 Hidden Gems by Engagement Rate (Task 4)"])

    with tab_likes:
        st.subheader("🔥 Top 10 Posts by Absolute Likes")
        fig_likes, top_likes_df = chart_top_posts_by_likes(filtered_df, top_n=10)
        st.plotly_chart(fig_likes, use_container_width=True)

        render_chart_takeaway(
            chart_title="Top 10 Posts by Likes",
            observation=f"The #1 post ({top_likes_df.iloc[-1]['Post_ID']}) achieved {top_likes_df['Likes'].max():,} likes, driven primarily by high-visibility Giveaway and Festive Offer campaigns.",
            business_meaning="Giveaway and seasonal promotion hooks generate instantaneous mass-market applause and tap into consumer excitement, generating large volumes of top-of-funnel validation.",
            action_item="Standardize the visual creative template of these top 10 posts as benchmark standards for future festive and product launch blitzes.",
            accent="pink"
        )

        st.markdown("#### 📋 Detailed Data for Top Posts by Likes")
        st.dataframe(
            top_likes_df[['Post_ID', 'Post Date', 'Post Type', 'Campaign Type', 'Likes', 'Comments', 'Saves', 'Reach', 'Engagement_Rate', 'Hashtags']]
            .sort_values('Likes', ascending=False),
            use_container_width=True,
            hide_index=True
        )

    with tab_er:
        st.subheader("💎 Top 10 Hidden Gem Posts by Engagement Rate")
        fig_er, top_er_df = chart_top_posts_by_engagement_rate(filtered_df, top_n=10)
        st.plotly_chart(fig_er, use_container_width=True)

        render_chart_takeaway(
            chart_title="Top 10 Hidden Gems by Engagement Rate",
            observation=f"Hidden gem content achieved astronomical engagement rates upwards of {top_er_df['Engagement_Rate'].max():.1f}%, often in Tutorial and Product Launch formats.",
            business_meaning="These posts triggered intense community resonance (high saves, comments, and shares) despite having lower algorithmic reach, signaling immense viral latent potential.",
            action_item="Allocate paid boost budget to these high-ER hidden gem posts to expand their distribution to broader lookalike beauty audiences.",
            accent="gold"
        )

        st.markdown("#### 📋 Detailed Data for Top Hidden Gems")
        st.dataframe(
            top_er_df[['Post_ID', 'Post Date', 'Post Type', 'Campaign Type', 'Engagement_Rate', 'Likes', 'Comments', 'Shares', 'Saves', 'Reach', 'Hashtags']]
            .sort_values('Engagement_Rate', ascending=False),
            use_container_width=True,
            hide_index=True
        )

# ------------------------------------------
# PAGE 4: POST FORMAT BENCHMARK (Task 5)
# ------------------------------------------
elif selected_page.startswith("🎨 4."):
    render_brand_header(
        title="Post Format & Creative Performance Comparison",
        subtitle="Cross-analyzing Reels, Stories, Videos, and Static Images across key interaction types"
    )

    render_about_section(
        section_name="Creative Format Optimization: Reels vs Images vs Videos vs Stories",
        description="This section addresses <b>Task 5: Post Type Performance Comparison</b>. Different Instagram media formats fulfill distinct roles in the marketing funnel: Reels drive discovery and virality, Stories nurture daily loyalty, Videos demonstrate detailed tutorials, and static Images communicate crisp aesthetics. This view evaluates average likes, comments, saves, shares, and conversion rates across all four formats to guide production budgets.",
        key_questions=[
            "Which post format delivers the highest average likes, comments, and saves?",
            "Are video assets (Reels & Videos) outperforming static assets in viewer retention?",
            "How should the Sugar Cosmetics creative studio allocate its weekly production budget?"
        ],
        metrics_tracked=[
            "Average Likes per Format", "Average Comments per Format", "Average Saves per Format", "Average Shares per Format", "Format Share of Voice"
        ]
    )

    fig_format, format_agg = chart_post_type_comparison(filtered_df)
    st.plotly_chart(fig_format, use_container_width=True)

    render_chart_takeaway(
        chart_title="Post Type Comparative Performance",
        observation="Across the 50,000 post sample, all four formats (Reels, Stories, Videos, Images) demonstrate remarkably balanced baseline engagement (~2,950 likes, ~370 comments, and ~175 saves per post), with Reels and Videos exhibiting edge leadership in shares and comments.",
        business_meaning="Sugar Cosmetics has established strong creative execution across formats; format fatigue is avoided because the content mix is well balanced across tutorials, launches, and offers.",
        action_item="Deploy Reels primarily for user acquisition and viral reach, while utilizing Carousel/Image posts for detailed step-by-step beauty routines and ingredient breakdowns.",
        accent="pink"
    )

    # Secondary Drilldown Table & Radar
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.subheader("📊 Format Performance Scorecard")
        st.dataframe(
            format_agg.rename(columns={
                'Post Type': 'Format',
                'Avg_Likes': 'Avg Likes',
                'Avg_Comments': 'Avg Comments',
                'Avg_Saves': 'Avg Saves',
                'Avg_Shares': 'Avg Shares',
                'Avg_Reach': 'Avg Reach',
                'Avg_ER': 'Avg ER (%)'
            }).style.format({
                'Avg Likes': '{:,.1f}',
                'Avg Comments': '{:,.1f}',
                'Avg Saves': '{:,.1f}',
                'Avg Shares': '{:,.1f}',
                'Avg Reach': '{:,.1f}',
                'Avg ER (%)': '{:.2f}%'
            }),
            use_container_width=True,
            hide_index=True
        )

    with col_r:
        st.subheader("🎯 Format Share of Content Mix")
        type_counts = filtered_df['Post Type'].value_counts().reset_index()
        type_counts.columns = ['Post Type', 'Count']
        import plotly.express as px
        fig_donut = px.pie(
            type_counts,
            names='Post Type',
            values='Count',
            hole=0.5,
            color='Post Type',
            color_discrete_sequence=["#FF007F", "#9D4EDD", "#00E5FF", "#FFB703"]
        )
        fig_donut.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#CBD5E1")
        )
        st.plotly_chart(fig_donut, use_container_width=True)

# ------------------------------------------
# PAGE 5: DAY-OF-WEEK OPTIMIZATION (Task 6)
# ------------------------------------------
elif selected_page.startswith("📅 5."):
    render_brand_header(
        title="Day-of-Week Scheduling & Timing Optimization",
        subtitle="Uncovering audience active rhythms and optimal weekly publishing windows"
    )

    render_about_section(
        section_name="Temporal Intelligence & Publishing Schedule",
        description="This section addresses <b>Task 6: Day of Week Analysis</b>. User engagement on Instagram fluctuates significantly between weekdays and weekends due to work routines, commuting hours, and leisure browsing patterns. By extracting day names from publication dates, this analysis pinpoints when the Sugar Cosmetics community is most receptive to interaction, enabling maximum reach per published asset.",
        key_questions=[
            "Which days of the week produce the highest average engagement rates?",
            "Do weekends outperform weekdays in total comment velocity and viral shares?",
            "What is the recommended weekly content publishing schedule for maximum ROI?"
        ],
        metrics_tracked=[
            "Engagement Rate by Day", "Average Reach by Day", "Comment Velocity by Day", "Weekday vs Weekend Spread"
        ]
    )

    fig_dow, dow_df = chart_day_of_week_analysis(filtered_df)
    st.plotly_chart(fig_dow, use_container_width=True)

    render_chart_takeaway(
        chart_title="Day of Week Engagement Distribution",
        observation="Engagement rates remain consistently high across all days of the week (18.4% - 18.6%), with mid-week (Wednesday/Thursday) and weekend (Saturday/Sunday) exhibiting peak active commenting and share velocity.",
        business_meaning="The Sugar Cosmetics audience maintains high daily affinity, consuming beauty content on weekdays during breaks/commutes and engaging in weekend leisurely makeup tutorials.",
        action_item="Schedule major product drops and influencer collaborative reveals on Wednesday-Thursday, while saving weekend slots for community UGC, tutorials, and festive giveaway entries.",
        accent="gold"
    )

    # Detailed weekday breakdown
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.subheader("📅 Weekday vs. Weekend Aggregate Performance")
        ww_agg = filtered_df.groupby('Is_Weekend').agg(
            Posts=('Reach', 'count'),
            Avg_Reach=('Reach', 'mean'),
            Avg_ER=('Engagement_Rate', 'mean'),
            Total_Likes=('Likes', 'sum')
        ).reset_index()
        ww_agg['Type'] = ww_agg['Is_Weekend'].map({0: 'Weekday (Mon-Fri)', 1: 'Weekend (Sat-Sun)'})

        import plotly.express as px
        fig_ww = px.bar(
            ww_agg,
            x='Type',
            y='Avg_ER',
            color='Type',
            text=ww_agg['Avg_ER'].apply(lambda x: f"{x:.2f}%"),
            color_discrete_map={'Weekday (Mon-Fri)': '#9D4EDD', 'Weekend (Sat-Sun)': '#FF007F'},
            title="<b>Average Engagement Rate: Weekdays vs. Weekends</b>"
        )
        fig_ww.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(19, 23, 34, 0.6)",
            font=dict(color="#CBD5E1"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.07)")
        )
        st.plotly_chart(fig_ww, use_container_width=True)

    with col_w2:
        st.subheader("📋 Day-of-Week Metric Scorecard")
        st.dataframe(
            dow_df.rename(columns={
                'Day_Name': 'Day',
                'Avg_ER': 'Avg ER (%)',
                'Avg_Reach': 'Avg Reach',
                'Avg_Likes': 'Avg Likes',
                'Avg_Comments': 'Avg Comments',
                'Post_Count': 'Posts Published'
            }).style.format({
                'Avg ER (%)': '{:.2f}%',
                'Avg Reach': '{:,.1f}',
                'Avg Likes': '{:,.1f}',
                'Avg Comments': '{:,.1f}',
                'Posts Published': '{:,}'
            }),
            use_container_width=True,
            hide_index=True
        )

# ------------------------------------------
# PAGE 6: AUDIENCE ENGAGEMENT FUNNEL (Task 7)
# ------------------------------------------
elif selected_page.startswith("🌪️ 6."):
    render_brand_header(
        title="Audience Engagement & Conversion Funnel",
        subtitle="Tracking viewer progression from exposure to unique reach and high-intent actions"
    )

    render_about_section(
        section_name="Social Media Interaction Funnel & Drop-off Analysis",
        description="This section addresses <b>Task 7: Engagement Funnel</b>. Modern social media analytics requires viewing audience touchpoints as a progressive marketing funnel: <b>Impressions → Unique Reach → Likes → Comments → Shares → Saves</b>. Analyzing drop-off rates at each transition reveals where user interest is highest and where audience engagement leaks occur, allowing targeted tactical interventions.",
        key_questions=[
            "How efficiently do gross impressions convert into unique audience reach?",
            "What percentage of viewers transition from passive liking to active conversation (comments)?",
            "What is the viral multiplier (shares) and evergreen intent (saves) through the funnel?"
        ],
        metrics_tracked=[
            "Gross Impressions", "Unique Reach", "Likes", "Comments", "Shares", "Saves", "Stage Drop-off Ratios"
        ]
    )

    fig_funnel, funnel_vals = chart_engagement_funnel(filtered_df)
    st.plotly_chart(fig_funnel, use_container_width=True)

    render_chart_takeaway(
        chart_title="Funnel Progression & Drop-Off Dynamics",
        observation=f"From {funnel_vals['Impressions']:,} Impressions, {funnel_vals['Unique Reach']:,} Unique Accounts were reached (77.4% conversion). From Unique Reach, {funnel_vals['Likes']:,} Likes were generated (15.0% conversion), progressing to {funnel_vals['Comments']:,} Comments (12.5% of likes) and {funnel_vals['Saves']:,} Saves.",
        business_meaning="The funnel exhibits healthy top-of-funnel reach capture. The drop-off from Likes to Comments/Shares is consistent with industry norms for consumer beauty, highlighting that lightweight likes are easy to capture while comments require conversational prompts.",
        action_item="Integrate interactive conversation starters in post captions (e.g., 'Comment shade 01 or 02 below!') to systematically boost the Likes-to-Comments stage conversion rate above 15%.",
        accent="pink"
    )

    # Conversion Rate Metrics Table
    st.subheader("📊 Funnel Conversion Step Metrics")
    f_c1, f_c2, f_c3, f_c4 = st.columns(4)
    with f_c1:
        render_kpi_card("Reach per Impression", f"{(funnel_vals['Unique Reach']/funnel_vals['Impressions'])*100:.1f}%", "Unique viewer penetration", "Healthy Breadth")
    with f_c2:
        render_kpi_card("Likes per Reach", f"{(funnel_vals['Likes']/funnel_vals['Unique Reach'])*100:.1f}%", "Top-level approval rate", "Industry Benchmark")
    with f_c3:
        render_kpi_card("Comments per Like", f"{(funnel_vals['Comments']/funnel_vals['Likes'])*100:.1f}%", "Conversation depth ratio", "Community Dialogue")
    with f_c4:
        render_kpi_card("Saves per Like", f"{(funnel_vals['Saves']/funnel_vals['Likes'])*100:.1f}%", "High-value reference ratio", "Evergreen Intent")

# ------------------------------------------
# PAGE 7: HASHTAG & CAMPAIGN STRATEGY (Task 8)
# ------------------------------------------
elif selected_page.startswith("🏷️ 7."):
    render_brand_header(
        title="Hashtag Performance & Campaign Deep-Dive",
        subtitle="Evaluating campaign pillars, audience emotional sentiment, and hashtag discovery efficiency"
    )

    render_about_section(
        section_name="Content Categorization: Hashtags, Campaigns, and Emotions",
        description="This section addresses <b>Task 8: Hashtag Analysis</b> and explores strategic content dimensions. Hashtags are key discovery catalysts on Instagram. Here we analyze the effectiveness of core brand hashtags (#CrueltyFree, #MakeupGoals, #VeganBeauty, #BoldLooks, #SugarCosmetics) alongside campaign pillars (Tutorial, Giveaway, Festive Offer, Product Launch, Influencer Collab) and audience emotional resonance.",
        key_questions=[
            "Which hashtags drive superior average engagement rates and discovery reach?",
            "Which campaign types produce the highest volume of comments and profile visits?",
            "What audience emotion (Inspired, Confident, Excited, Happy, Curious) resonates strongest?"
        ],
        metrics_tracked=[
            "Hashtag Occurrence Frequency", "Average ER by Hashtag", "Campaign Type Performance", "Audience Emotion Correlation"
        ]
    )

    col_h1, col_h2 = st.columns([1.2, 1])
    with col_h1:
        st.subheader("🏷️ Average Engagement Rate by Hashtag")
        fig_hash, hash_agg = chart_hashtag_performance(filtered_df)
        st.plotly_chart(fig_hash, use_container_width=True)

        render_chart_takeaway(
            chart_title="Hashtag Impact on Engagement",
            observation="Core ethical and beauty values (#CrueltyFree, #VeganBeauty) perform on par with aspirational tags (#MakeupGoals, #BoldLooks) with average engagement rates tightly clustered around 18.5%.",
            business_meaning="Sugar Cosmetics' brand positioning naturally bridges cruelty-free ethical beauty with bold, high-glamour aesthetics. Audiences respond enthusiastically to both value propositions.",
            action_item="Bundle complementary hashtags (e.g., pair #CrueltyFree with #BoldLooks) on every post to capture both value-conscious and style-driven audience segments simultaneously.",
            accent="blue"
        )

    with col_h2:
        st.subheader("📦 Campaign Type Performance")
        fig_camp, camp_df = chart_campaign_type_distribution(filtered_df)
        st.plotly_chart(fig_camp, use_container_width=True)

        render_chart_takeaway(
            chart_title="Campaign Type Contribution",
            observation="Tutorials and Giveaways generate high engagement, while Product Launches and Influencer Collabs drive direct profile discovery and follower acquisition.",
            business_meaning="Each campaign type serves a distinct role in the brand ecosystem: Giveaways for top-of-funnel buzz, and Tutorials for mid-funnel education and purchase intent.",
            action_item="Maintain a 40/30/20/10 content mix: 40% Tutorials, 30% Influencer Collabs, 20% Product Launches, and 10% High-Impact Giveaways.",
            accent="gold"
        )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # Audience Emotion & Channel Hierarchy
    st.subheader("✨ Audience Emotion & Channel Synergy Breakdown")
    fig_sun = chart_emotion_and_source_sunburst(filtered_df)
    st.plotly_chart(fig_sun, use_container_width=True)

    render_chart_takeaway(
        chart_title="Emotion & Channel Synergy",
        observation="Content invoking 'Inspired' and 'Excited' emotions generates the deepest engagement across Collab and Organic sources.",
        business_meaning="Cosmetics is an emotive and confidence-enhancing category. Content that empowers self-expression consistently outperforms sterile product showcases.",
        action_item="Center creative briefs around empowering messaging—'Be Bold, Be You'—leveraging genuine customer transformation stories.",
        accent="pink"
    )

# ------------------------------------------
# PAGE 8: STRATEGIC RECOMMENDATIONS (Task 10)
# ------------------------------------------
elif selected_page.startswith("🎯 8."):
    render_brand_header(
        title="Strategic Marketing Recommendations",
        subtitle="Data-driven executive action plan, posting playbook, and campaign roadmap for Sugar Cosmetics"
    )

    render_about_section(
        section_name="Executive Action Plan & Strategic Roadmap",
        description="This section addresses <b>Task 10: Strategic Recommendations</b>. Grounded in quantitative findings from 50,000 Instagram posts, this strategic brief provides actionable guidelines for brand leadership, creative directors, and performance marketers. It synthesizes findings on posting timing, content formats, hashtag strategies, identified performance gaps, and proposed campaign concepts.",
        key_questions=[
            "What are the top data-driven takeaways for Sugar Cosmetics' social media strategy?",
            "What is the recommended posting cadence, format mix, and optimal timing?",
            "What operational gaps were uncovered and what novel campaign initiatives should be launched?"
        ],
        metrics_tracked=[
            "Data Insights Summary", "Strategic Recommendations", "Identified Gaps", "Campaign Concepts"
        ]
    )

    st.markdown("""
    ### 💎 Key Strategic Takeaways from Data Analytics

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px; margin-bottom: 25px;">
        <div style="background: #141724; border: 1px solid rgba(255, 0, 127, 0.3); border-radius: 12px; padding: 20px;">
            <div style="font-size: 1.1rem; font-weight: 700; color: #FF007F; margin-bottom: 8px;">1. Robust Baseline Community Health</div>
            <p style="font-size: 0.9rem; color: #CBD5E1; line-height: 1.6;">
                Sugar Cosmetics maintains an outstanding average engagement rate of <strong>~18.5%</strong> across all channels, far exceeding the typical beauty industry benchmark of 1.5% - 3.5%. This indicates genuine brand love, loyal customer resonance, and strong content relevance.
            </p>
        </div>
        <div style="background: #141724; border: 1px solid rgba(0, 229, 255, 0.3); border-radius: 12px; padding: 20px;">
            <div style="font-size: 1.1rem; font-weight: 700; color: #00E5FF; margin-bottom: 8px;">2. Multi-Format Omnipresence</div>
            <p style="font-size: 0.9rem; color: #CBD5E1; line-height: 1.6;">
                Reels and Videos generate high comment counts and viral shares, while Stories maintain daily dialogue and Images anchor aesthetic product packaging. Equal allocation across formats prevents audience fatigue and maximizes multi-surface algorithm placement.
            </p>
        </div>
        <div style="background: #141724; border: 1px solid rgba(255, 183, 3, 0.3); border-radius: 12px; padding: 20px;">
            <div style="font-size: 1.1rem; font-weight: 700; color: #FFB703; margin-bottom: 8px;">3. Ethical & Glamour Synergy</div>
            <p style="font-size: 0.9rem; color: #CBD5E1; line-height: 1.6;">
                Hashtags emphasizing cruelty-free and vegan formulations (#CrueltyFree, #VeganBeauty) generate equal engagement velocity to glam tags (#BoldLooks, #MakeupGoals). Customers actively value ethical beauty when combined with bold pigmentation.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("🚀 Tactical Playbook & Posting Strategy")

    rec_c1, rec_c2 = st.columns(2)
    with rec_c1:
        st.markdown("""
        #### ⏰ Timing & Frequency Optimization
        - **Publishing Schedule:** Deploy prime educational and product launch reels on **Wednesday and Thursday evenings (6:00 PM - 9:00 PM IST)** to capitalize on peak mid-week commute and evening browsing habits.
        - **Weekend Strategy:** Utilize Saturdays and Sundays for user-generated content (UGC), quick weekend look challenges, and giveaway entry reminders.
        - **Consistency Target:** Maintain a steady cadence of **3-4 feed posts daily** (mix of 2 Reels, 1 Image/Carousel, 1 Video) complemented by **6-8 interactive Stories**.
        """)

        st.markdown("""
        #### 🔄 Conversion & Follower Growth Tactics
        - **Frictionless Save CTAs:** Conclude every tutorial video with a direct prompt: *"Save this reel so you don't lose the shade codes!"* Increasing save rates boosts long-term explore page discovery.
        - **Profile Visit Hooks:** Utilize bio link incentives (e.g. exclusive coupon codes announced exclusively on Stories) to raise the profile visit rate from 3.0% to 5.0%.
        """)

    with rec_c2:
        st.markdown("""
        #### ⚠️ Gaps Identified & Corrective Actions
        - **Gap 1: Comment-to-Like Ratio Drop-off:** While likes are abundant, comments represent 12.5% of like volume.
          - *Fix:* End captions with binary choice questions: *"Which shade are you rocking this Friday: Red Terror or Matte Plum? Drop 1 or 2 below!"*
        - **Gap 2: Hidden Gem Under-Monetization:** Dozens of high-engagement posts have limited reach due to organic algorithm throttling.
          - *Fix:* Implement an automated weekly workflow to allocate paid boost ad spend ($100-$300 per post) behind organic posts that exceed a 25% engagement threshold within the first 4 hours of posting.
        """)

        st.markdown("""
        #### 💡 Proposed Content & Campaign Concepts
        1. **#SugarBoldReels Challenge:** A community transformation campaign where creators switch from bare face to a bold signature look in a 7-second audio transition.
        2. **"Makeup Simplified" 30-Day Masterclass:** Daily bite-sized tutorial reels addressing specific consumer pain points (e.g. eyeliner symmetry, foundation shade matching).
        3. **Clean Glamour Spotlight:** A transparent behind-the-scenes series highlighting Sugar's certified vegan and cruelty-free formulation standards.
        """)

# ------------------------------------------
# PAGE 9: INTERACTIVE DATA EXPLORER
# ------------------------------------------
elif selected_page.startswith("🔍 9."):
    render_brand_header(
        title="Interactive Data Explorer & Export Engine",
        subtitle="Search, slice, filter, and export preprocessed Sugar Cosmetics performance data"
    )

    render_about_section(
        section_name="Raw & Processed Data Management",
        description="This section provides access to the complete underlying dataset of <b>50,000 preprocessed Instagram posts</b>. You can search by post ID or caption keyword, filter by custom KPI thresholds, choose specific columns to inspect, and download customized CSV slices for external reporting or team analysis.",
        key_questions=[
            "How can marketing analysts inspect individual post attributes and calculated KPIs?",
            "How can we download specific filtered segments (e.g. high-engagement Reels) for agency partners?"
        ],
        metrics_tracked=[
            "Data Filtering", "Column Selection", "Quick Search", "CSV Data Export"
        ]
    )

    st.subheader(f"📋 Filtered Dataset ({len(filtered_df):,} matching posts)")

    # Search bar & column multi-select
    s_col1, s_col2 = st.columns([1.5, 2])
    with s_col1:
        search_query = st.text_input("🔍 Search by Post ID, Caption, or Hashtag:", placeholder="e.g. POST-00120 or #CrueltyFree")
    with s_col2:
        all_cols = filtered_df.columns.tolist()
        default_cols = ['Post_ID', 'Post Date', 'Post Type', 'Campaign Type', 'Engagement_Rate', 'Reach', 'Likes', 'Comments', 'Shares', 'Saves', 'Hashtags']
        selected_cols = st.multiselect("Visible Columns:", all_cols, default=[c for c in default_cols if c in all_cols])

    display_df = filtered_df.copy()
    if search_query:
        display_df = display_df[
            display_df['Post_ID'].astype(str).str.contains(search_query, case=False, na=False) |
            display_df['Caption'].astype(str).str.contains(search_query, case=False, na=False) |
            display_df['Hashtags'].astype(str).str.contains(search_query, case=False, na=False)
        ]

    st.dataframe(
        display_df[selected_cols].head(500),
        use_container_width=True,
        hide_index=True
    )
    if len(display_df) > 500:
        st.info(f"Showing first 500 of {len(display_df):,} matching rows. Download full CSV below.")

    # CSV Download button
    csv_bytes = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Dataset as CSV",
        data=csv_bytes,
        file_name="sugar_cosmetics_filtered_instagram_data.csv",
        mime="text/csv",
        help="Export current slice of data with all calculated KPIs for external presentation or reporting."
    )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.subheader("📊 Summary Statistics of Current Selection")
    st.dataframe(display_df[['Reach', 'Impressions', 'Likes', 'Comments', 'Shares', 'Saves', 'Engagement_Rate', 'Profile Visits', 'Follows']].describe(), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.8rem; padding: 15px 0;">
    <strong>Sugar Cosmetics Instagram Performance Analytics Dashboard</strong> • Built for Executive Social Media & Business Intelligence Teams<br>
    Data Source: sugar_cosmetics_instagram_data.csv (50,000 records) • Interactive Streamlit & Plotly Platform
</div>
""", unsafe_allow_html=True)
