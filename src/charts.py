"""
Plotly Chart Generators for Sugar Cosmetics Analytics Dashboard
Follows high-end corporate cosmetics aesthetic with dark palette,
glowing pink/magenta accents, and responsive layout.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Corporate Brand Palette
COLOR_PRIMARY = "#FF007F"     # Sugar Signature Magenta
COLOR_SECONDARY = "#9D4EDD"   # Electric Purple
COLOR_CYAN = "#00E5FF"        # Vibrant Cyan
COLOR_GOLD = "#FFB703"        # Amber Gold
COLOR_GREEN = "#10B981"       # Mint Green
COLOR_RED = "#EF4444"         # Crimson
COLOR_PALETTE = ["#FF007F", "#00E5FF", "#9D4EDD", "#FFB703", "#10B981", "#F43F5E", "#8B5CF6"]

THEME_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(19, 23, 34, 0.6)",
    font=dict(family="Plus Jakarta Sans, sans-serif", color="#CBD5E1", size=12),
    margin=dict(l=40, r=40, t=50, b=40),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(size=11, color="#E2E8F0")
    ),
    xaxis=dict(
        gridcolor="rgba(255, 255, 255, 0.07)",
        zerolinecolor="rgba(255, 255, 255, 0.12)",
        tickfont=dict(color="#94A3B8")
    ),
    yaxis=dict(
        gridcolor="rgba(255, 255, 255, 0.07)",
        zerolinecolor="rgba(255, 255, 255, 0.12)",
        tickfont=dict(color="#94A3B8")
    )
)

def chart_monthly_posting_trend(df):
    """Task 2: Monthly Posting Trend & Consistency Over Time."""
    trend = df.groupby('Year_Month').agg(
        Post_Count=('Reach', 'count'),
        Avg_Reach=('Reach', 'mean'),
        Avg_Engagement_Rate=('Engagement_Rate', 'mean'),
        Total_Interactions=('Total_Interactions', 'sum')
    ).reset_index().sort_values('Year_Month')

    fig = go.Figure()

    # Bar for post volume
    fig.add_trace(go.Bar(
        x=trend['Year_Month'],
        y=trend['Post_Count'],
        name="Posts Published",
        marker=dict(
            color='rgba(255, 0, 127, 0.45)',
            line=dict(color=COLOR_PRIMARY, width=1.5)
        ),
        yaxis="y",
        hovertemplate="<b>%{x}</b><br>Posts Published: %{y:,}<extra></extra>"
    ))

    # Line for Average Engagement Rate
    fig.add_trace(go.Scatter(
        x=trend['Year_Month'],
        y=trend['Avg_Engagement_Rate'],
        name="Avg Engagement Rate (%)",
        mode="lines+markers",
        line=dict(color=COLOR_CYAN, width=3),
        marker=dict(size=7, color=COLOR_CYAN, symbol="circle"),
        yaxis="y2",
        hovertemplate="<b>%{x}</b><br>Avg Engagement Rate: %{y:.2f}%<extra></extra>"
    ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text="<b>Monthly Posting Volume vs. Engagement Rate Trajectory</b>", font=dict(size=15, color="#FFFFFF")),
        yaxis=dict(title="Posts Published", gridcolor="rgba(255, 255, 255, 0.07)", tickfont=dict(color="#94A3B8")),
        yaxis2=dict(
            title="Avg Engagement Rate (%)",
            overlaying="y",
            side="right",
            showgrid=False,
            tickfont=dict(color=COLOR_CYAN)
        ),
        hovermode="x unified"
    )
    fig.update_layout(layout)
    return fig

def chart_top_posts_by_likes(df, top_n=10):
    """Task 3: Top Posts by Likes."""
    top_df = df.nlargest(top_n, 'Likes').sort_values('Likes', ascending=True)
    top_df['Display_Label'] = top_df.apply(
        lambda r: f"{r['Post_ID']} | {r['Post Type']} ({r['Campaign Type'][:12]})", axis=1
    )

    fig = go.Figure(go.Bar(
        x=top_df['Likes'],
        y=top_df['Display_Label'],
        orientation='h',
        marker=dict(
            color=top_df['Likes'],
            colorscale=[[0, '#800040'], [0.5, '#FF007F'], [1, '#FF7597']],
            line=dict(color='#FFA3C2', width=1)
        ),
        text=top_df['Likes'].apply(lambda x: f"{x:,.0f} likes"),
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Likes: %{x:,}<extra></extra>"
    ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text=f"<b>Top {top_n} Instagram Posts by Total Likes</b>", font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title="Total Likes Received", gridcolor="rgba(255, 255, 255, 0.07)"),
        yaxis=dict(title="Post Reference", automargin=True),
        height=450
    )
    fig.update_layout(layout)
    return fig, top_df

def chart_top_posts_by_engagement_rate(df, top_n=10):
    """Task 4: Top Posts by Engagement Rate (Hidden Gems)."""
    top_df = df.nlargest(top_n, 'Engagement_Rate').sort_values('Engagement_Rate', ascending=True)
    top_df['Display_Label'] = top_df.apply(
        lambda r: f"{r['Post_ID']} | {r['Post Type']} ({r['Campaign Type'][:12]})", axis=1
    )

    fig = go.Figure(go.Bar(
        x=top_df['Engagement_Rate'],
        y=top_df['Display_Label'],
        orientation='h',
        marker=dict(
            color=top_df['Engagement_Rate'],
            colorscale=[[0, '#005f73'], [0.5, '#0a9396'], [1, '#94d2bd']],
            line=dict(color='#00E5FF', width=1)
        ),
        text=top_df['Engagement_Rate'].apply(lambda x: f"{x:.2f}%"),
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Engagement Rate: %{x:.2f}%<br>Reach: %{customdata[0]:,}<br>Likes: %{customdata[1]:,}<extra></extra>",
        customdata=top_df[['Reach', 'Likes']].values
    ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text=f"<b>Top {top_n} Hidden Gem Posts by Engagement Rate (% of Reach)</b>", font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title="Engagement Rate (%)", gridcolor="rgba(255, 255, 255, 0.07)"),
        yaxis=dict(title="Post Reference", automargin=True),
        height=450
    )
    fig.update_layout(layout)
    return fig, top_df

def chart_post_type_comparison(df):
    """Task 5: Post Type Performance Comparison across key metrics."""
    agg = df.groupby('Post Type').agg(
        Avg_Likes=('Likes', 'mean'),
        Avg_Comments=('Comments', 'mean'),
        Avg_Saves=('Saves', 'mean'),
        Avg_Shares=('Shares', 'mean'),
        Avg_Reach=('Reach', 'mean'),
        Avg_ER=('Engagement_Rate', 'mean')
    ).reset_index()

    categories = ['Avg Likes', 'Avg Comments', 'Avg Saves', 'Avg Shares']

    fig = go.Figure()
    for _, row in agg.iterrows():
        fig.add_trace(go.Bar(
            name=row['Post Type'],
            x=categories,
            y=[row['Avg_Likes'], row['Avg_Comments'], row['Avg_Saves'], row['Avg_Shares']],
            hovertemplate="<b>%{x}</b>: %{y:,.1f}<extra>" + row['Post Type'] + "</extra>"
        ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text="<b>Post Type Benchmark: Interactions per Post Format</b>", font=dict(size=15, color="#FFFFFF")),
        barmode='group',
        colorway=COLOR_PALETTE,
        xaxis=dict(title="Interaction Type", gridcolor="rgba(255,255,255,0.07)"),
        yaxis=dict(title="Average per Post", gridcolor="rgba(255,255,255,0.07)"),
        height=450
    )
    fig.update_layout(layout)
    return fig, agg

def chart_day_of_week_analysis(df):
    """Task 6: Day of Week Engagement Analysis."""
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dow = df.groupby('Day_Name').agg(
        Avg_ER=('Engagement_Rate', 'mean'),
        Avg_Reach=('Reach', 'mean'),
        Avg_Likes=('Likes', 'mean'),
        Avg_Comments=('Comments', 'mean'),
        Post_Count=('Reach', 'count')
    ).reindex(day_order).reset_index()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=dow['Day_Name'],
        y=dow['Avg_ER'],
        name="Avg Engagement Rate (%)",
        marker=dict(
            color=dow['Avg_ER'],
            colorscale=[[0, '#3A0CA3'], [0.5, '#7209B7'], [1, '#F72585']],
            line=dict(color="#FF007F", width=1.5)
        ),
        text=dow['Avg_ER'].apply(lambda x: f"{x:.2f}%"),
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Avg Engagement Rate: %{y:.2f}%<extra></extra>"
    ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text="<b>Engagement Rate by Day of the Week</b>", font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title="Day of Week", gridcolor="rgba(255, 255, 255, 0.07)"),
        yaxis=dict(title="Average Engagement Rate (%)", gridcolor="rgba(255, 255, 255, 0.07)"),
        height=420
    )
    fig.update_layout(layout)
    return fig, dow

def chart_engagement_funnel(df):
    """Task 7: Engagement Funnel: Impressions -> Reach -> Likes -> Comments -> Shares -> Saves."""
    total_imp = df['Impressions'].sum()
    total_reach = df['Reach'].sum()
    total_likes = df['Likes'].sum()
    total_comments = df['Comments'].sum()
    total_shares = df['Shares'].sum()
    total_saves = df['Saves'].sum()

    stages = ['Impressions', 'Unique Reach', 'Likes', 'Comments', 'Shares', 'Saves']
    values = [total_imp, total_reach, total_likes, total_comments, total_shares, total_saves]

    fig = go.Figure(go.Funnel(
        y=stages,
        x=values,
        textinfo="value+percent previous",
        texttemplate="<b>%{y}</b><br>%{value:,.0f} (%{percentPrevious:.1%})",
        marker=dict(
            color=['#4A0E4E', '#800080', '#C71585', '#FF007F', '#FF69B4', '#FFB6C1'],
            line=dict(width=1, color="rgba(255, 255, 255, 0.4)")
        ),
        connector=dict(line=dict(color="rgba(255, 0, 127, 0.4)", width=2))
    ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text="<b>Sugar Cosmetics Content Conversion Funnel</b>", font=dict(size=15, color="#FFFFFF")),
        height=480
    )
    fig.update_layout(layout)
    return fig, dict(zip(stages, values))

def chart_hashtag_performance(df):
    """Task 8: Hashtag Performance Analysis."""
    # Explode hashtags to evaluate individual hashtag metrics
    records = []
    for _, row in df.iterrows():
        tags = [t.strip() for t in str(row['Hashtags']).split(',') if t.strip()]
        for tag in tags:
            records.append({
                'Hashtag': tag,
                'Reach': row['Reach'],
                'Impressions': row['Impressions'],
                'Likes': row['Likes'],
                'Comments': row['Comments'],
                'Saves': row['Saves'],
                'Shares': row['Shares'],
                'Total_Interactions': row['Total_Interactions'],
                'Engagement_Rate': row['Engagement_Rate']
            })
    
    tag_df = pd.DataFrame(records)
    agg = tag_df.groupby('Hashtag').agg(
        Post_Occurrences=('Reach', 'count'),
        Avg_Reach=('Reach', 'mean'),
        Avg_ER=('Engagement_Rate', 'mean'),
        Avg_Likes=('Likes', 'mean'),
        Avg_Saves=('Saves', 'mean')
    ).reset_index().sort_values('Avg_ER', ascending=False)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=agg['Hashtag'],
        y=agg['Avg_ER'],
        name="Avg Engagement Rate (%)",
        marker=dict(
            color=agg['Avg_ER'],
            colorscale=[[0, '#1E3A8A'], [0.5, '#3B82F6'], [1, '#60A5FA']],
            line=dict(color=COLOR_CYAN, width=1.5)
        ),
        text=agg['Avg_ER'].apply(lambda x: f"{x:.2f}%"),
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Avg Engagement Rate: %{y:.2f}%<br>Occurrences: %{customdata:,}<extra></extra>",
        customdata=agg['Post_Occurrences']
    ))

    layout = THEME_LAYOUT.copy()
    layout.update(
        title=dict(text="<b>Average Engagement Rate by Hashtag</b>", font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title="Hashtag", gridcolor="rgba(255, 255, 255, 0.07)"),
        yaxis=dict(title="Avg Engagement Rate (%)", gridcolor="rgba(255, 255, 255, 0.07)"),
        height=420
    )
    fig.update_layout(layout)
    return fig, agg

def chart_campaign_type_distribution(df):
    """Campaign Type Analysis across Engagement Rate and Volume."""
    camp = df.groupby('Campaign Type').agg(
        Posts=('Reach', 'count'),
        Avg_Reach=('Reach', 'mean'),
        Avg_ER=('Engagement_Rate', 'mean'),
        Total_Likes=('Likes', 'sum'),
        Total_Follows=('Follows', 'sum')
    ).reset_index().sort_values('Avg_ER', ascending=False)

    fig = px.treemap(
        camp,
        path=['Campaign Type'],
        values='Posts',
        color='Avg_ER',
        color_continuous_scale=[[0, '#2D0A31'], [0.5, '#9A1F6E'], [1, '#FF007F']],
        title="<b>Campaign Types: Volume (Box Size) vs Engagement Rate (Color)</b>"
    )
    fig.update_traces(
        textinfo="label+value+percent parent",
        hovertemplate="<b>%{label}</b><br>Posts: %{value:,}<br>Avg ER: %{color:.2f}%<extra></extra>"
    )
    layout = THEME_LAYOUT.copy()
    layout.update(height=420)
    fig.update_layout(layout)
    return fig, camp

def chart_emotion_and_source_sunburst(df):
    """Engagement Source vs Audience Emotion Multi-dimensional Drilldown."""
    agg = df.groupby(['Engagement Source', 'Audience Emotion']).agg(
        Total_Interactions=('Total_Interactions', 'sum'),
        Avg_ER=('Engagement_Rate', 'mean')
    ).reset_index()

    fig = px.sunburst(
        agg,
        path=['Engagement Source', 'Audience Emotion'],
        values='Total_Interactions',
        color='Avg_ER',
        color_continuous_scale='Purp',
        title="<b>Engagement Source & Audience Emotion Hierarchy</b>"
    )
    layout = THEME_LAYOUT.copy()
    layout.update(height=450)
    fig.update_layout(layout)
    return fig
