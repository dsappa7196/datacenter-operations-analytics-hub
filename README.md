# 🏢 Data Center Operations Analytics Hub
### End-to-End Analytics Solution | Power BI · SQL · Python · Star Schema

<div align="center">

![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-Data%20Engineering-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Star%20Schema-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-Data%20Center%20Ops-1a1a2e?style=for-the-badge)

**[▶ Open Interactive Dashboard](https://dsappa7196-github-io-yjma.vercel.app/analytics-hub)** · [📊 See Key Findings](#-key-findings) · [🏗 Architecture](#-solution-architecture)**

</div>

---

## 🎯 What This Project Is — And Why It Exists

> *"We have a lot of data, but it's not necessarily all in one place."*  
> — Common challenge in large-scale data center operations

This project simulates a **real-world analytics challenge** faced by data center operators managing multiple sites, assets, and teams across regions. The goal was not to build *a dashboard* — it was to build **the analytics infrastructure that makes ongoing decision-making possible**.

Most analytics projects stop at visualization. This one doesn't. It covers:

| Layer | What It Does |
|-------|-------------|
| 📦 **Data Foundation** | 5 fact tables + 3 dimension tables in a production star schema |
| 🔄 **Integration** | Cross-domain data unified from operations, maintenance, finance, assets, and customer systems |
| 📊 **Dashboard Suite** | 6 interactive decision-support views in Power BI |
| 🏠 **Access Hub** | Centralized portal so stakeholders go to *one place*, not many reports |
| 💡 **Insights Layer** | Structured narrative: What → Why → What to do |

---

## 👩‍💼 Who Built This & Why

**Built by: Padmasree (Padma) Sappa**  
Senior Business Analyst | Analytics & Reporting | San Francisco, CA

📎 Linkedin: https://www.linkedin.com/in/padmasreesappa/ · 📁 Portfolio: (https://dsappa7196-github-io-yjma.vercel.app/) · 📧 sdnps7196@gmail.com

### My Background
I have 6+ years of experience turning messy, multi-system data into **decisions** — not just reports. I've done this at Amazon (brand protection analytics, $1M business impact), at CGI (Jira delivery forecasting, 30% improvement in sprint accuracy), and across cross-functional teams in operations and finance.

### Why I Built This Specific Project
I wanted to demonstrate exactly the kind of work I do best:
- **Not just dashboards** — a full analytics *solution* with a data model, access layer, and insight narrative
- **Multi-domain integration** — connecting asset, maintenance, operations, finance, and customer data that live in silos
- **Business-first thinking** — every chart answers a decision question, not just displays a metric
- **Scalability** — built so a team can extend it, not just the person who built it

This is the kind of infrastructure a reporting team actually needs. It reduces manual work, enables self-service for stakeholders, and creates a sustainable foundation for ongoing analytics.

---

## 📐 Solution Architecture![Solution Architecture](architecture%20diagram.png)

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                             │
│  Operations · Maintenance · Finance · Assets · Customer CX      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DATA FOUNDATION (SQL)                        │
│                                                                 │
│   DIMENSION TABLES          FACT TABLES                         │
│   ├── site_dim          ──▶ operations_daily (6,564 rows)       │
│   ├── date_dim          ──▶ maintenance_work_orders (7,761 rows) │
│   └── assets            ──▶ finance_monthly (864 rows)          │
│                         ──▶ installed_customer_base (216 rows)  │
│                         ──▶ customer_experience (216 rows)      │
│                                                                 │
│   Star Schema · Grain-aligned · Relationship-validated          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  ANALYTICS LAYER (Power BI)                     │
│                                                                 │
│   ├── Executive Overview      ├── Asset Intelligence            │
│   ├── Operations & Incidents  ├── Finance & Spend               │
│   ├── Maintenance Analytics   └── Customer Experience           │
│                                                                 │
│   DAX Measures · Time Intelligence · Cross-filter ready         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              ACCESS & COMMUNICATION LAYER                       │
│                                                                 │
│   Analytics Hub (centralized portal) · Insight narratives       │
│   Stakeholder-ready summaries · Action-oriented recommendations │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Data Model — Star Schema

**5 Fact Tables · 3 Dimension Tables · 12 Sites · 18 Months of Data**

```
                    ┌──────────────┐
                    │   date_dim   │
                    │  (547 rows)  │
                    └──────┬───────┘
                           │ year_month / date_key
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼──────┐   ┌───────▼──────┐  ┌───────▼──────┐
│ operations   │   │  finance     │  │  customer_cx │
│ _daily       │   │  _monthly    │  │  _monthly    │
│ (6,564 rows) │   │  (864 rows)  │  │  (216 rows)  │
└───────┬───────┘   └──────────────┘  └──────────────┘
        │ site_code
┌───────▼──────────────────────────────────────────┐
│                   site_dim                        │
│   (12 sites · region · country · capacity_mw)    │
└───────┬──────────────────────────────────────────┘
        │
        ├─── maintenance_work_orders (7,761 rows)
        │         └── asset_id ──▶ assets (540 rows)
        │
        └─── installed_customer_base (216 rows)
```

---

## 🔍 Key Findings

These are real analytical conclusions drawn from the dataset — the kind a reporting analyst surfaces for leadership:

### 🔴 Critical
| Finding | Detail | Business Impact |
|---------|--------|----------------|
| **DAL01 (Dallas) is highest-risk** | Availability: 99.678% vs 99.9% SLA target | SLA breach risk · customer churn exposure |
| **40.8% of work orders breach SLA** | Systemic across all sites, not one-off | Process gap requiring escalation |
| **Cooling assets: 63.6% repair-to-replace ratio** | Repair costs exceeding asset value threshold | Replacement planning needed |

### 🟡 Monitor
| Finding | Detail | Business Impact |
|---------|--------|----------------|
| **Structural overspend every month** | +$5.4M cumulative · Power Opex the main driver | Budget reforecasting required |
| **CSAT dipped Jul–Dec 2024** | Correlated with incident spike at specific sites | Customer retention risk |
| **107 assets flagged for review** | Condition score below threshold | Lifecycle planning gap |

### 🟢 Positive Signal
| Finding | Detail |
|---------|--------|
| **SEA01 (Seattle) is strongest performer** | Highest availability · lowest incident rate |
| **Preventive maintenance ratio improving** | Trending from reactive toward proactive |
| **CSAT partially recovered Q1 2025** | Aligned with incident reduction in same period |

---

## 📁 Repository Structure

```
data-center-analytics-hub/
│
├── 📄 README.md
│
├── 📂 data/
│   ├── raw/
│   │   ├── operations_daily.csv          # 6,564 rows · daily ops metrics
│   │   ├── maintenance_work_orders.csv   # 7,761 rows · full work order history
│   │   ├── finance_monthly.csv           # 864 rows · budget vs actual
│   │   ├── assets.csv                    # 540 assets · condition + lifecycle
│   │   ├── customer_experience_monthly.csv
│   │   ├── installed_customer_base_monthly.csv
│   │   ├── site_dim.csv                  # 12 sites · metadata + capacity
│   │   └── date_dim.csv                  # 547 dates · time intelligence
│   └── data_dictionary.csv               # 105 fields fully documented
│
├── 📂 sql/
│   └── star_schema_relationships.sql     # Table definitions + join logic
│
├── 📂 dashboards/
│   ├── Equinix_Unified_Analytics_Hub.html    # Full interactive dashboard
│   ├── analytics_hub_access_layer.html       # Centralized portal / hub page
│   └── operations_analytics_dashboard.html   # Operations-focused view
│
├── 📂 docs/
│   ├── architecture_diagram.png          # Solution architecture (full)
│   ├── data_model_diagram.png            # Star schema visual
│   └── build_guide.pdf                   # Full technical build documentation
│
└── 📂 assets/
    └── screenshots/                      # Dashboard screenshots
```

---

## 🛠 Tech Stack & Skills Demonstrated

| Category | Tools / Skills |
|----------|---------------|
| **Data Engineering** | Python · pandas · CSV ingestion · data validation · schema design |
| **Database** | SQL · MySQL · Star schema modeling · dimensional modeling |
| **Analytics** | Power BI · DAX measures · time intelligence · KPI framework design |
| **Visualization** | Multi-page dashboard design · drill-through · cross-filter |
| **Communication** | Insight narrative structure · stakeholder-ready reporting · access hub design |
| **Domain Knowledge** | Data center ops · asset lifecycle · SLA management · CSAT/NPS · OpEx/CapEx |

---

## 🧠 How I Approached This — My Analytical Process

This wasn't "pick a dataset, make charts." Here's how I actually worked:

**1. Understand the business questions first**  
Before touching data, I mapped the decisions stakeholders actually need to make: *Which site needs attention? Are we spending more to fix an asset than to replace it? Why did CSAT drop?*

**2. Design the data model to support those questions**  
A star schema was the right choice here — it allows any combination of site/date/domain filtering without query complexity. I aligned grain across all fact tables to `year_month` + `site_code`.

**3. Build the insight before the visual**  
For each dashboard view, I wrote the "so what" first: *DAL01 has a 99.678% availability rate against a 99.9% SLA — that gap compounds over 18 months into 5,945 downtime hours.* The visual came second.

**4. Design for the person who inherits this**  
I documented the data dictionary (105 fields), added metric definitions to the hub page, and structured the dashboard so someone unfamiliar can orient in 60 seconds.

---

## 💼 What This Demonstrates for Hiring Managers

If you're a recruiter or hiring manager — here's the direct translation:

✅ **Can join a new team and make sense of unfamiliar data fast** — this dataset had no manual, just raw CSVs across 5 domains  
✅ **Builds for reuse, not one-time delivery** — star schema + hub access layer = something a team can extend  
✅ **Translates data into decisions, not just charts** — every dashboard view answers a business question  
✅ **Communicates to non-technical stakeholders** — insight narrative structured as What → Why → Recommend  
✅ **Thinks about the full solution** — data model + dashboards + access + communication, not just one layer  
✅ **Works independently and delivers** — this is a solo end-to-end build  

---

## 📬 Let's Connect

I'm currently open to roles in **analytics, reporting, and business intelligence** — especially where the work involves building sustainable analytics infrastructure, not just ad-hoc reports.

If this project is relevant to what your team needs, I'd love to talk.

📧 sdnps7196@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/padmasreesappa/
🌐 Portfolio: https://dsappa7196-github-io-yjma.vercel.app/

---

<div align="center">

*Built with care, curiosity, and a belief that good analytics should answer questions — not just display numbers.*

</div>
