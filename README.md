# 💄 Sugar Cosmetics — Instagram Performance Analytics & BI Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sugar-cosmetics-instagram-analytics-av7p84ongrzh22foq5ft5r.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.58.0-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-6.7.0-3F4F75?logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **🚀 Live Interactive Web Dashboard:**  
> 👉 **[https://sugar-cosmetics-instagram-analytics-av7p84ongrzh22foq5ft5r.streamlit.app/](https://sugar-cosmetics-instagram-analytics-av7p84ongrzh22foq5ft5r.streamlit.app/)**

---

## 📌 Executive Overview & Problem Statement

**Sugar Cosmetics** is one of India's fastest-growing omni-channel beauty and cosmetics brands, renowned for bold, high-pigment, vegan, and cruelty-free makeup. Operating in an intensely visual and competitive direct-to-consumer (D2C) landscape, maintaining social media audience affinity, engagement velocity, and conversion efficiency is vital for customer acquisition and brand equity.

This project delivers an enterprise-grade **Social Media Business Intelligence & Growth Analytics Dashboard** built in **Python**, **Streamlit**, and **Plotly** (replacing traditional static Tableau / Power BI reports). Analyzing **50,000 verified Instagram posts** spanning a full operating calendar year (April 2024 to April 2025), the platform models reach dynamics, format efficacy, viral mechanics, community sentiment, and funnel drop-offs.

---

## 🏗️ Project Structure

```text
sugar-cosmetics-instagram-analytics/
│
├── .streamlit/
│   └── config.toml                           # Cloud theme & headless server configuration
│
├── data/
│   ├── raw/
│   │   └── sugar_cosmetics_instagram_data.csv# Standardized source raw dataset (50,000 records)
│   └── processed/
│       ├── sugar_cosmetics_cleaned.csv       # Preprocessed dataset with 35 engineered KPI fields
│       └── preprocessing_summary.txt         # Automated data audit report & descriptive metrics
│
├── src/
│   ├── __init__.py                           # Source package initializer
│   ├── data_preprocessing.py                 # Reproducible ETL, cleansing, and feature engineering
│   ├── data_loader.py                        # Cached streaming loader & multi-dimensional filtering
│   ├── components.py                         # Brand UI components: 'About Section' & 'Chart Takeaways'
│   └── charts.py                             # Corporate Plotly dark-luxury visualizations
│
├── app.py                                    # Main multi-view Streamlit enterprise BI application
├── requirements.txt                          # Production dependency specifications
├── run_dashboard.bat                         # 1-click Windows local launcher script
├── push_to_github.bat                        # Git synchronization script
├── .gitignore                                # Version control exclusion rules
└── README.md                                 # Full project documentation & architectural guide
```

### 📂 File Breakdown & Responsibilities
- **`app.py`**: Central application containing routing, sidebar navigation, filter management, layout grid, and page assemblies.
- **`src/data_preprocessing.py`**: Standalone, automated data cleaning script that handles datetime parsing, interaction summation, rate normalizations, and hashtag tokenization.
- **`src/data_loader.py`**: Implements `@st.cache_data` for instant sub-second filter slicing across 50,000 rows.
- **`src/components.py`**: Encapsulates Sugar Cosmetics' custom CSS theme (`#FF007F` electric magenta / dark obsidian) and renders mandatory top **About Sections** and bottom **Chart Takeaways**.
- **`src/charts.py`**: Plotly visualization factory with custom dual-axis plots, horizontal ranking bars, conversion funnels, treemaps, and sunburst charts.

---

## 🎨 Enterprise Dashboard Standards

Every page in this platform adheres to strict corporate BI guidelines:
1. **ℹ️ Top "About This Page" Guide:** Every view begins with an executive summary defining the business rationale, core metrics analyzed, and primary strategic questions addressed.
2. **💡 Bottom "Chart Insight & Strategic Takeaway" Cards:** Every visualization features an analytical briefing structured into:
   - 📌 **Data Finding:** Direct quantitative observation.
   - 💡 **Business Impact:** Operational significance for Sugar Cosmetics' marketing leadership.
   - 🚀 **Recommended Action:** Tactical next step for content and performance teams.
3. **🎛️ Dynamic Sidebar Filtering:** Real-time multi-select filters for Date Range, Post Type, Campaign Type, Engagement Source, Hashtags, and Audience Emotion.

---

## 📊 Analytical Views & Project Tasks Covered

| View | Page Title | Task Addressed | Strategic Deliverables & Visuals |
| :---: | :--- | :--- | :--- |
| **1** | **🏢 Executive Summary & KPIs** | **Task 1: Overview KPIs** | • 8 Macro scorecards: Total Posts (50k), Reach (987M+), Impressions (1.28B+), Likes, Comments, Saves, ER (18.54%)<br>• Community Interaction Distribution Donut<br>• Reach & ER by Channel Source Bar Chart |
| **2** | **📈 Monthly Posting Trends** | **Task 2: Monthly Posting Trend** | • Dual-Axis Monthly Posting Volume vs. Engagement Rate Trajectory<br>• Gross Impressions vs. Unique Reach Growth Area Chart |
| **3** | **🏆 Top Content & Hidden Gems** | **Tasks 3 & 4: Top by Likes & ER** | • **Top 10 Posts by Likes:** Mainstream viral reach drivers<br>• **Top 10 Hidden Gems by ER (%):** High-converting niche hooks |
| **4** | **🎨 Post Format Benchmark** | **Task 5: Post Type Comparison** | • Comparative Interaction Benchmark: Reels vs. Stories vs. Videos vs. Static Images across Likes, Comments, Saves, Shares<br>• Content Mix Share of Voice |
| **5** | **📅 Day-of-Week Optimization** | **Task 6: Day of Week Analysis** | • Day of Week Engagement Rate Bar Chart (Monday to Sunday)<br>• Weekday vs. Weekend comparative performance scorecards |
| **6** | **🌪️ Audience Engagement Funnel** | **Task 7: Engagement Funnel** | • 6-Stage Interactive Conversion Funnel: $\text{Impressions} \rightarrow \text{Reach} \rightarrow \text{Likes} \rightarrow \text{Comments} \rightarrow \text{Shares} \rightarrow \text{Saves}$<br>• Stage-by-stage drop-off ratios & health benchmarks |
| **7** | **🏷️ Hashtag & Campaign Strategy** | **Task 8: Hashtag Analysis** | • Average Engagement Rate by Hashtag (#CrueltyFree, #VeganBeauty, #BoldLooks, etc.)<br>• Campaign Type Treemap & Audience Emotion Sunburst |
| **8** | **🎯 Strategic Recommendations** | **Task 10: Strategic Recommendations** | • Executive Playbook: Publishing cadence, content format allocation, community engagement levers, gap remediation & campaign proposals |
| **9** | **🔍 Interactive Data Explorer** | **Data Governance & Audit** | • Searchable, filterable tabular dataset with column selectors, summary statistics, and one-click filtered CSV export |

---

## 📐 Data Preprocessing & Calculated KPI Metrics

The pipeline processes raw Instagram logs and generates standardized analytical columns:

1. **Temporal Dimensions:** Datetime extraction into `Year`, `Month`, `Year_Month` (e.g., `2024-05`), `Day_Name`, `Day_of_Week` (0-6), `Is_Weekend`.
2. **Total Community Interactions:**
   $$\text{Total Interactions} = \text{Likes} + \text{Comments} + \text{Shares} + \text{Saves}$$
   *(50,000 posts generated **183,164,417** total interactions).*
3. **Engagement Rate by Reach (Industry Standard):**
   $$\text{Engagement Rate} = \left(\frac{\text{Total Interactions}}{\text{Reach}}\right) \times 100 \quad (\text{Brand Average: } \mathbf{18.54\%})$$
4. **Engagement Rate by Impressions:**
   $$\text{Engagement Rate}_{\text{Imp}} = \left(\frac{\text{Total Interactions}}{\text{Impressions}}\right) \times 100$$
5. **Granular Action & Intent Ratios:**
   - $\text{Like Rate} = (\text{Likes} / \text{Reach}) \times 100$
   - $\text{Comment Rate} = (\text{Comments} / \text{Reach}) \times 100$
   - $\text{Save Rate (Evergreen Score)} = (\text{Saves} / \text{Reach}) \times 100$
   - $\text{Share Rate (Virality Score)} = (\text{Shares} / \text{Reach}) \times 100$
6. **Follower Conversion Efficiency:**
   $$\text{Follow Conversion Rate} = \left(\frac{\text{Follows}}{\text{Profile Visits}}\right) \times 100 \quad (\text{Brand Average: } \mathbf{29.78\%})$$
7. **Value Retention Score:**
   $$\text{Save-to-Like Ratio} = \left(\frac{\text{Saves}}{\text{Likes}}\right) \times 100$$

---

## 💡 Key Strategic Takeaways & Executive Insights

1. **Exceptional Account Health:** Sugar Cosmetics demonstrates an average engagement rate of **18.54%**, far exceeding the direct beauty industry median (1.5%–3.5%). 
2. **Balanced Content Mix:** All 4 formats (Reels, Stories, Videos, Images) sustain high parity in volume (~25% each) and baseline engagement (~2,950 likes, ~370 comments, ~175 saves per post). Reels lead in shares, while Carousels and Images drive save intent.
3. **Ethical Beauty Resonates Equally with Glamour:** Content tagged with `#CrueltyFree` and `#VeganBeauty` matches engagement velocity with aspirational tags like `#BoldLooks` and `#MakeupGoals`.
4. **Publishing Rhythms:** Wednesday and Thursday evenings produce optimal comment depth for product drops, while weekends drive leisure tutorial consumption and giveaway participation.

---

## 💻 Local Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Git installed

### 1. Clone the Repository
```bash
git clone https://github.com/Number789Alpha/sugar-cosmetics-instagram-analytics.git
cd sugar-cosmetics-instagram-analytics
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
# Option A: Command Line
streamlit run app.py

# Option B: Windows 1-Click Batch File
.\run_dashboard.bat
```
Open **`http://localhost:8501`** in your browser.

---

## 🛠️ Tech Stack & Libraries

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)
- **Data Manipulation & Preprocessing:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Interactive Visualizations:** [Plotly Express & Graph Objects](https://plotly.com/python/)
- **Styling:** Custom CSS, Google Fonts (*Plus Jakarta Sans*, *Space Grotesk*)
- **Hosting & Cloud CI/CD:** [Streamlit Community Cloud](https://share.streamlit.io/)

---

## 👤 Author
**Priyank Mishra**  
- GitHub: [@Number789Alpha](https://github.com/Number789Alpha)  
- Focus: Data Analytics • Business Intelligence • Python • SQL • Streamlit • Plotly

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
