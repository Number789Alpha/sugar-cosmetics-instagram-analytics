# 💄 Sugar Cosmetics: Instagram Performance Analytics Dashboard

An enterprise-grade social media intelligence and business analytics platform built with **Streamlit** and **Plotly**, designed specifically for **Sugar Cosmetics'** digital marketing and growth leadership teams.

---

## 📌 Executive Overview
This project replaces static BI tools (Tableau / Power BI) with a responsive, high-performance web analytics application that processes and visualizes **50,000 verified Instagram posts**.

### ✨ Highlights & Architecture
- **🎨 Brand Aesthetics:** Styled in Sugar Cosmetics' signature dark luxury cosmetic palette (Electric Pink `#FF007F`, Neon Magenta, Rich Charcoal `#0B0D13`, and subtle glassmorphic glow effects).
- **ℹ️ Mandatory About Sections:** Every single dashboard view features a dedicated, prominent **About This Page** container at the top explaining page objectives, key metrics tracked, and business questions answered.
- **💡 Graph Insight Cards:** Every visualization is followed by a **Chart Insight & Strategic Takeaway** callout card providing:
  - 📌 **Data Finding:** Direct numeric observation.
  - 💡 **Business Impact:** Operational meaning for Sugar Cosmetics.
  - 🚀 **Recommended Action:** Immediate actionable advice for the marketing team.
- **⚡ High Performance:** Automated data preprocessing pipeline with cached streaming (<0.2s filter response times).
- **🎛️ Global Sidebar Filters:** Real-time filtering across Date Range, Post Type, Campaign Type, Engagement Source, Hashtags, and Audience Emotion.

---

## 📂 Project Structure

```text
├── data/
│   ├── raw/
│   │   └── sugar_cosmetics_instagram_data.csv    # Source raw dataset
│   └── processed/
│       ├── sugar_cosmetics_cleaned.csv           # Cleaned & engineered data (50k rows, 35 cols)
│       └── preprocessing_summary.txt             # Data audit & KPI summary
├── src/
│   ├── data_preprocessing.py                     # ETL pipeline & calculated KPI fields
│   ├── data_loader.py                            # Streamlit caching & interactive filtering
│   ├── components.py                             # Reusable cards, about boxes, takeaway pills
│   └── charts.py                                 # Plotly enterprise dark-theme visualizations
├── app.py                                        # Streamlit multi-view enterprise dashboard
├── run_dashboard.bat                             # One-click Windows startup script
└── README.md                                     # Complete project documentation
```

---

## 📊 Analytical Views & Tasks Covered

| Page | View Title | Task Addressed | Primary Metrics & Focus |
| :--- | :--- | :--- | :--- |
| **1** | **Executive Summary & KPIs** | Task 1: Overview KPIs | Total Posts, Reach (987M+), Impressions (1.27B+), Likes, Comments, Saves, ER (18.54%) |
| **2** | **Monthly Posting Trends** | Task 2: Monthly Posting Trend | Monthly post consistency (~4.1k/mo), dual-axis volume vs. ER trajectory |
| **3** | **Top Content & Hidden Gems** | Tasks 3 & 4: Top by Likes & ER | Top 10 viral hits by likes, Top 10 high-conversion hidden gems, post details |
| **4** | **Post Format Benchmark** | Task 5: Post Type Comparison | Reels vs. Stories vs. Videos vs. Images across Likes, Comments, Saves, Shares |
| **5** | **Day-of-Week Optimization** | Task 6: Day of Week Analysis | Weekday vs. Weekend engagement, optimal publishing schedules (Wed/Thu/Sun) |
| **6** | **Audience Engagement Funnel** | Task 7: Engagement Funnel | Impressions → Reach → Likes → Comments → Shares → Saves drop-off analysis |
| **7** | **Hashtag & Campaign Strategy** | Task 8: Hashtag & Campaign Deep-Dive | #CrueltyFree, #VeganBeauty, #BoldLooks, Campaign pillars & Audience Emotion sunburst |
| **8** | **Strategic Recommendations** | Task 10: Strategic Recommendations | Actionable marketing playbook, budget re-allocation, content pillars, gap analysis |
| **9** | **Interactive Data Explorer** | Data Governance & Audit | Filterable data table, keyword search, column selector, full CSV export |

---

## 📐 Data Preprocessing & Calculated Fields

The data pipeline (`src/data_preprocessing.py`) handles:
1. **Datetime Conversion & Extraction:** `Year`, `Month`, `Year_Month` (e.g. `2024-05`), `Day_Name`, `Day_of_Week`, `Is_Weekend`.
2. **Total Interactions:** $\text{Likes} + \text{Comments} + \text{Shares} + \text{Saves}$.
3. **Engagement Rate (% by Reach):** $\frac{\text{Total Interactions}}{\text{Reach}} \times 100$ *(Avg: 18.54%)*.
4. **Engagement Rate (% by Impressions):** $\frac{\text{Total Interactions}}{\text{Impressions}} \times 100$.
5. **Action Rates:**
   - $\text{Like Rate} = (\text{Likes} / \text{Reach}) \times 100$
   - $\text{Comment Rate} = (\text{Comments} / \text{Reach}) \times 100$
   - $\text{Save Rate} = (\text{Saves} / \text{Reach}) \times 100$
   - $\text{Share Rate} = (\text{Shares} / \text{Reach}) \times 100$
6. **Conversion Rates:**
   - $\text{Follow Conversion Rate} = (\text{Follows} / \text{Profile Visits}) \times 100$ *(Avg: 29.78%)*.
   - $\text{Save to Like Ratio} = (\text{Saves} / \text{Likes}) \times 100$.

---

## 🚀 How to Run the Dashboard

### Prerequisites
Python 3.10+ installed with `pandas`, `streamlit`, and `plotly`.

### Option A: One-Click Startup (Windows)
Double click `run_dashboard.bat` or run:
```powershell
.\run_dashboard.bat
```

### Option B: Manual Command Line
```powershell
# 1. Run Preprocessing Pipeline (optional, already completed)
python src/data_preprocessing.py

# 2. Launch Streamlit Dashboard
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.
