"""
Data Preprocessing & KPI Calculation Pipeline
Project: Instagram Performance Analytics for Sugar Cosmetics
Domain: Digital Marketing | Social Media Analytics | Business Intelligence
"""

import os
import shutil
import pandas as pd
import numpy as np

def run_preprocessing():
    print("=" * 60)
    print("[INFO] Starting Sugar Cosmetics Instagram Data Preprocessing Pipeline")
    print("=" * 60)

    # 1. Paths
    raw_source = "sugar_cosmetics_instagram_data - sugar_cosmetics_instagram_data.csv.csv"
    raw_dest = os.path.join("data", "raw", "sugar_cosmetics_instagram_data.csv")
    processed_dest = os.path.join("data", "processed", "sugar_cosmetics_cleaned.csv")
    summary_dest = os.path.join("data", "processed", "preprocessing_summary.txt")

    os.makedirs(os.path.dirname(raw_dest), exist_ok=True)
    os.makedirs(os.path.dirname(processed_dest), exist_ok=True)

    # Copy to standardized raw path
    if os.path.exists(raw_source) and not os.path.exists(raw_dest):
        shutil.copyfile(raw_source, raw_dest)
        print(f"[OK] Raw dataset copied to: {raw_dest}")
    elif os.path.exists(raw_dest):
        print(f"[INFO] Raw dataset already present at: {raw_dest}")

    file_to_read = raw_dest if os.path.exists(raw_dest) else raw_source
    df = pd.read_csv(file_to_read)
    initial_shape = df.shape
    print(f"[INFO] Loaded raw data: {initial_shape[0]:,} rows, {initial_shape[1]} columns")

    # 2. Standardize column names (snake_case and clean strip)
    df.columns = [col.strip() for col in df.columns]

    # Check for missing values & duplicates
    missing_counts = df.isnull().sum()
    duplicate_count = df.duplicated().sum()
    print(f"[INFO] Duplicate rows: {duplicate_count}")
    print(f"[INFO] Missing values:\n{missing_counts[missing_counts > 0] if missing_counts.sum() > 0 else 'None (0 missing)'}")

    # 3. Datetime parsing & temporal feature extraction
    df['Post Date'] = pd.to_datetime(df['Post Date'])
    df['Year'] = df['Post Date'].dt.year
    df['Month'] = df['Post Date'].dt.month
    df['Year_Month'] = df['Post Date'].dt.to_period('M').astype(str)
    df['Month_Name'] = df['Post Date'].dt.strftime('%B')
    df['Day_Name'] = df['Post Date'].dt.strftime('%A')
    df['Day_of_Week'] = df['Post Date'].dt.dayofweek # Monday=0, Sunday=6
    df['Is_Weekend'] = df['Day_of_Week'].isin([5, 6]).astype(int)

    # 4. Content & Interaction Calculations
    # Total Interactions = Likes + Comments + Shares + Saves
    df['Total_Interactions'] = df['Likes'] + df['Comments'] + df['Shares'] + df['Saves']

    # Safeguard against zero reach or impressions
    df['Reach'] = df['Reach'].replace(0, np.nan)
    df['Impressions'] = df['Impressions'].replace(0, np.nan)

    # Core Social Media KPIs
    # Engagement Rate relative to Reach (%) - Industry Standard
    df['Engagement_Rate'] = (df['Total_Interactions'] / df['Reach']) * 100
    # Engagement Rate relative to Impressions (%)
    df['Engagement_Rate_Imp'] = (df['Total_Interactions'] / df['Impressions']) * 100

    # Interaction breakdown ratios
    df['Like_Rate'] = (df['Likes'] / df['Reach']) * 100
    df['Comment_Rate'] = (df['Comments'] / df['Reach']) * 100
    df['Share_Rate'] = (df['Shares'] / df['Reach']) * 100
    df['Save_Rate'] = (df['Saves'] / df['Reach']) * 100

    # High-value actions
    df['Profile_Visit_Rate'] = (df['Profile Visits'] / df['Reach']) * 100
    # Follow conversion: of people who visited profile, what % followed
    df['Follow_Conversion_Rate'] = np.where(
        df['Profile Visits'] > 0,
        (df['Follows'] / df['Profile Visits']) * 100,
        0.0
    )

    # Virality & Evergreen Quality Scores
    # Virality: High shares per 1,000 Reach
    df['Virality_Score'] = (df['Shares'] / df['Reach']) * 1000
    # Evergreen / Value Score: Saves per 100 Likes
    df['Save_to_Like_Ratio'] = np.where(df['Likes'] > 0, (df['Saves'] / df['Likes']) * 100, 0.0)

    # 5. Hashtag processing
    # Create clean hashtag list column and hashtag count
    def parse_hashtags(val):
        if pd.isna(val):
            return []
        return [t.strip() for t in str(val).split(',') if t.strip()]

    df['Hashtag_List'] = df['Hashtags'].apply(parse_hashtags)
    df['Hashtag_Count'] = df['Hashtag_List'].apply(len)
    df['Primary_Hashtag'] = df['Hashtag_List'].apply(lambda x: x[0] if len(x) > 0 else 'None')

    # 6. Save clean dataset
    # For CSV export, convert Hashtag_List to string representation
    df_export = df.copy()
    df_export['Hashtag_List'] = df_export['Hashtag_List'].apply(lambda l: ";".join(l))
    df_export.to_csv(processed_dest, index=False)
    print(f"[OK] Clean processed dataset saved to: {processed_dest} ({df_export.shape[0]:,} rows, {df_export.shape[1]} cols)")

    # 7. Generate Summary Text Report
    summary_report = f"""SUGAR COSMETICS INSTAGRAM DATASET PREPROCESSING AUDIT
======================================================
Raw records: {initial_shape[0]:,}
Clean records: {len(df):,}
Date Range: {df['Post Date'].min().strftime('%Y-%m-%d')} to {df['Post Date'].max().strftime('%Y-%m-%d')}
Total Days Covered: {(df['Post Date'].max() - df['Post Date'].min()).days} days

KEY PERFORMANCE TOTALS & AVERAGES:
----------------------------------
Total Posts Published: {len(df):,}
Total Impressions: {df['Impressions'].sum():,}
Total Reach: {df['Reach'].sum():,}
Total Likes: {df['Likes'].sum():,}
Total Comments: {df['Comments'].sum():,}
Total Shares: {df['Shares'].sum():,}
Total Saves: {df['Saves'].sum():,}
Total Profile Visits: {df['Profile Visits'].sum():,}
Total Follows Gained: {df['Follows'].sum():,}

AVERAGE METRICS PER POST:
------------------------
Average Reach: {df['Reach'].mean():,.1f}
Average Likes: {df['Likes'].mean():,.1f}
Average Comments: {df['Comments'].mean():,.1f}
Average Shares: {df['Shares'].mean():,.1f}
Average Saves: {df['Saves'].mean():,.1f}
Average Engagement Rate (by Reach): {df['Engagement_Rate'].mean():.2f}%
Average Follow Conversion Rate: {df['Follow_Conversion_Rate'].mean():.2f}%

POST TYPES BREAKDOWN:
--------------------
{df['Post Type'].value_counts().to_string()}

CAMPAIGN TYPES BREAKDOWN:
------------------------
{df['Campaign Type'].value_counts().to_string()}
======================================================
Status: Ready for Streamlit Dashboard consumption.
"""

    with open(summary_dest, 'w', encoding='utf-8') as f:
        f.write(summary_report)

    print(f"[OK] Preprocessing summary written to: {summary_dest}")
    print("=" * 60)
    print("[SUCCESS] Preprocessing Complete!")
    print("=" * 60)
    return df

if __name__ == "__main__":
    run_preprocessing()
