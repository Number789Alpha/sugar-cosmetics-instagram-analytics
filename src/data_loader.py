"""
Data Loader and Filtering Utility for Sugar Cosmetics Streamlit Dashboard
Handles fast cached loading, filtering, and metric aggregations.
"""

import os
import pandas as pd
import numpy as np
import streamlit as st

DATA_PATH = os.path.join("data", "processed", "sugar_cosmetics_cleaned.csv")
RAW_PATH = os.path.join("data", "raw", "sugar_cosmetics_instagram_data.csv")
BACKUP_PATH = "sugar_cosmetics_instagram_data - sugar_cosmetics_instagram_data.csv.csv"

@st.cache_data(show_spinner=False)
def load_data():
    """Load and prepare data with automatic fallback and caching."""
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
    elif os.path.exists(RAW_PATH):
        from src.data_preprocessing import run_preprocessing
        df = run_preprocessing()
    elif os.path.exists(BACKUP_PATH):
        from src.data_preprocessing import run_preprocessing
        df = run_preprocessing()
    else:
        raise FileNotFoundError("Could not locate Sugar Cosmetics Instagram dataset.")

    df['Post Date'] = pd.to_datetime(df['Post Date'])
    if 'Post_ID' not in df.columns:
        df['Post_ID'] = [f"POST-{i+1:05d}" for i in range(len(df))]
    
    # Generate informative post headline / caption if not already present
    if 'Caption' not in df.columns or df['Caption'].isnull().all():
        df['Caption'] = df.apply(
            lambda r: f"✨ {r['Campaign Type']} Spotlight: Unleash your beauty with our {r['Post Type']}! {r['Hashtags']} #SugarObsessed",
            axis=1
        )
    
    return df

def apply_filters(df, date_range=None, post_types=None, campaign_types=None, sources=None, emotions=None, selected_hashtag=None):
    """Apply interactive sidebar filters to dataframe."""
    filtered_df = df.copy()

    if date_range and len(date_range) == 2:
        start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        filtered_df = filtered_df[(filtered_df['Post Date'] >= start_date) & (filtered_df['Post Date'] <= end_date)]

    if post_types:
        filtered_df = filtered_df[filtered_df['Post Type'].isin(post_types)]

    if campaign_types:
        filtered_df = filtered_df[filtered_df['Campaign Type'].isin(campaign_types)]

    if sources:
        filtered_df = filtered_df[filtered_df['Engagement Source'].isin(sources)]

    if emotions:
        filtered_df = filtered_df[filtered_df['Audience Emotion'].isin(emotions)]

    if selected_hashtag and selected_hashtag != "All Hashtags":
        filtered_df = filtered_df[filtered_df['Hashtags'].str.contains(selected_hashtag, na=False, case=False)]

    return filtered_df

def compute_executive_kpis(df):
    """Compute high-level summary KPIs for scorecards."""
    total_posts = len(df)
    if total_posts == 0:
        return {
            'total_posts': 0, 'total_reach': 0, 'total_impressions': 0,
            'total_likes': 0, 'total_comments': 0, 'total_shares': 0,
            'total_saves': 0, 'total_visits': 0, 'total_follows': 0,
            'avg_engagement_rate': 0.0, 'avg_reach': 0.0, 'conversion_rate': 0.0,
            'virality_rate': 0.0, 'save_rate': 0.0
        }

    total_reach = df['Reach'].sum()
    total_impressions = df['Impressions'].sum()
    total_likes = df['Likes'].sum()
    total_comments = df['Comments'].sum()
    total_shares = df['Shares'].sum()
    total_saves = df['Saves'].sum()
    total_visits = df['Profile Visits'].sum()
    total_follows = df['Follows'].sum()
    total_interactions = total_likes + total_comments + total_shares + total_saves

    avg_er = (total_interactions / total_reach * 100) if total_reach > 0 else 0.0
    conv_rate = (total_follows / total_visits * 100) if total_visits > 0 else 0.0
    virality_rate = (total_shares / total_reach * 100) if total_reach > 0 else 0.0
    save_rate = (total_saves / total_reach * 100) if total_reach > 0 else 0.0

    return {
        'total_posts': total_posts,
        'total_reach': total_reach,
        'total_impressions': total_impressions,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'total_shares': total_shares,
        'total_saves': total_saves,
        'total_visits': total_visits,
        'total_follows': total_follows,
        'total_interactions': total_interactions,
        'avg_engagement_rate': avg_er,
        'avg_reach': df['Reach'].mean(),
        'conversion_rate': conv_rate,
        'virality_rate': virality_rate,
        'save_rate': save_rate
    }
