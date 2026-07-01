# 🔬 A/B Testing Pipeline with ETL Automation

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-0064a5.svg)
![Tableau](https://img.shields.io/badge/Tableau-Public-orange.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**End-to-End Data Analytics Project | Python • PostgreSQL • Tableau • GitHub Actions**
![Dashboard Preview]([docs/dashboard_screenshot.png](https://github.com/awaliahftr/ab-testing-pipeline/blob/6e858dff94c91f7c42c53a768842aedf81c9dee0/docs/dashboard.png))

---

## 🎯 Project Overview

This project demonstrates an **end-to-end A/B testing pipeline** with automated ETL (Extract, Transform, Load) and real-time dashboard monitoring.

### Problem Statement

> *"Does changing the button color from blue (A) to green (B) increase conversion rate?"*

### Business Context

In e-commerce, even small changes to user interface (like button color) can significantly impact conversion rates. A/B testing allows businesses to make data-driven decisions by comparing two versions of a webpage or app feature.

### Solution

We built an automated system that:
1. **Generates A/B test data daily** — Simulates 10,000 users per day with 50/50 split between Group A (blue button) and Group B (green button)
2. **Runs statistical analysis** — Chi-Square test to determine if Group B significantly outperforms Group A
3. **Sends email notifications** — Daily reports with results and business recommendations
4. **Updates Tableau dashboard** — Live connection to database keeps dashboard current

---

## 🧠 **Architecture & Data Flow**
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│ GitHub Actions (CI/CD)                                          │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Schedule: Daily at 8 AM                                 │     │
│ │                                                         │     │
│ │ 1. Generate Data (Python) → PostgreSQL (Supabase)       │     │
│ │ 2. ETL Pipeline (Python) → A/B Test Analysis            │     │
│ │ 3. Email Notification → Gmail (App Password)            │     │
│ │ 4. Push to Tableau → Live Dashboard                     │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ Tableau Dashboard                                               │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Live Connection to Supabase PostgreSQL                  │     │
│ │ • KPI Cards (Conv A, Conv B, Lift)                      │     │
│ │ • Bar Chart (Conversion Rate per Group)                 │     │
│ │ • P-Value & Significance Status                         │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ **Tech Stack**

| **Layer** | **Technologies** |
|-----------|------------------|
| **Programming** | Python 3.11 (Pandas, NumPy, SQLAlchemy, SciPy) |
| **Database** | PostgreSQL (Supabase Cloud) |
| **Visualization** | Tableau Public (Live Connection) |
| **CI/CD** | GitHub Actions (scheduled & manual) |
| **Email Notification** | Gmail SMTP (App Password) |
| **Version Control** | Git & GitHub |

---

## 📊 **Key Features**

### ✅ Automated Data Generation
- Generates **10,000 users** per day
- **50/50 split** between Group A and Group B
- **Conversion rate**: Group A ~10%, Group B ~15% (simulating real-world improvement)
- Timestamp tracking for each simulation

### ✅ ETL Pipeline
- **Extract**: Loads raw data from PostgreSQL (Supabase)
- **Transform**: 
  - Calculates conversion rate per group
  - Runs **Chi-Square test** for statistical significance
  - Computes **lift percentage** (relative improvement)
  - Aggregates results into summary table
- **Load**: Saves transformed data back to PostgreSQL

### ✅ Statistical Analysis (A/B Testing)
- **Chi-Square Test** for independence
- **P-Value**: 0.0000 (highly significant)
- **Lift**: 51.55% improvement (Group B over Group A)
- **Confidence Level**: 95%

### ✅ Email Reporting
- Automated email sent daily at 8:00 AM (WIB)
- Email contains:
  - Conversion rates (A & B)
  - Lift percentage
  - P-Value & significance status
  - Business recommendation (DEPLOY / DO NOT DEPLOY)

### ✅ Interactive Tableau Dashboard
- **Live connection** to Supabase PostgreSQL (data always current)
- **KPI Cards**: Total Users, Conversion Rate A, Conversion Rate B, Lift
- **Visualizations**: Bar Chart (Conversion Rate per Group), Significance Display
- **Business insights**: Clear recommendation based on statistical results

---

## 📈 **A/B Test Results**

| **Metric** | **Group A** | **Group B** |
|------------|-------------|-------------|
| **Users** | 5,076 | 4,924 |
| **Conversions** | 519 | 763 |
| **Conversion Rate** | 10.22% | **15.50%** |
| **Lift** | — | **+51.55%** |
| **P-Value** | — | **0.0000** ✅ |

### Interpretation

- **Statistically significant** (p < 0.05): The difference is real, not due to chance
- **Lift = +51.55%**: Group B is 51.55% better than Group A
- **Recommendation**: 🎯 **DEPLOY!** The green button significantly improves conversion

---

## 📁 **Project Structure**
```
ab-testing-pipeline/
├── .github/
│ └── workflows/
│ └── daily_etl.yml # GitHub Actions CI/CD workflow
├── scripts/
│ ├── generate_ab_data.py # Generate A/B test simulation data
│ └── etl_pipeline.py # ETL & statistical analysis
├── tableau/
│ └── ab_testing_dashboard.twbx 
├── docs/
│ └── dashboard_screenshot.png
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
## 🚀 **How to Run**

### **1️⃣ Clone Repository**

```
git clone https://github.com/awaliahftr/ab-testing-pipeline.git
cd ab-testing-pipeline

pip install -r requirements.txt
```

## 👤 Author
Awaliah Fitri Nur Ananda
- 🔗 LinkedIn: https://www.linkedin.com/in/awaliahftrr 
- 📧 Email: awaliahftrr@gmail.com

