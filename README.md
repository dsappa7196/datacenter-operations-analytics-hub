# Data Center Operations Analytics Hub

An end-to-end analytics solution built for multi-site data center operations — covering assets, maintenance, finance, and customer experience across 12 AMER sites.

**Stack:** Python · SQL · Power BI · HTML &nbsp;|&nbsp; **Domain:** Data Center Ops · Infrastructure Analytics

[▶ Open Live Dashboard](https://dsappa7196.github.io/datacenter-operations-analytics-hub/hub-content.html) &nbsp;·&nbsp; [Portfolio](https://dsappa7196-github-io-yjma.vercel.app/) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/padmasreesappa/)

---

![Solution Architecture](architecture%20diagram.png)

---

## Why This Project Exists

Data center operations teams manage assets, maintenance, finances, and customer relationships — but this data typically lives in separate systems. The result is manual pulls, one-off reports, and decisions made without a complete picture.

This project builds the infrastructure to change that: one data model, one hub, one place to go.

---

## What It Covers

| Layer | Description |
|---|---|
| Data Foundation | 5 fact tables + 3 dimension tables in a star schema, grain-aligned across all domains |
| Analytics Layer | 6 Power BI dashboard views — operations, maintenance, finance, assets, customer, executive |
| Access Hub | Centralized portal with metric definitions, ownership, and refresh schedule |
| Insight Narrative | Every finding structured as: what is happening → why → what to do |

---

## Data Model

```
date_dim (547 rows)
    ├── operations_daily         (6,564 rows)
    ├── finance_monthly          (  864 rows)
    └── customer_experience      (  216 rows)

site_dim (12 sites · AMER East, West, Central)
    ├── operations_daily
    ├── maintenance_work_orders  (7,761 rows)
    │       └── assets           (  540 rows)
    └── installed_customer_base  (  216 rows)
```

Many-to-one from fact to dimension. Supports cross-domain drill-down — site → assets → maintenance → financial impact — without query rewriting.

---

## Key Findings

**DAL01 (Dallas) — highest risk site.**
Availability at 99.678% vs. 99.9% SLA target. Compounds to 5,945 downtime hours over 18 months. Highest incident count, highest repair cost, lowest CSAT in the fleet.

**40.8% of work orders breach SLA.**
Consistent across all 12 sites — this is a systemic process gap, not a site-level anomaly.

**Spend is over budget every month.**
Cumulative variance of +$5.4M. Power OpEx is the primary driver. The overspend is structural.

**CSAT dropped Jul–Dec 2024, partially recovered Q1 2025.**
Correlates directly with the incident spike at specific sites in that period — operational performance and customer experience are measurably linked.

**SEA01 (Seattle) — strongest performer.**
Highest availability, lowest incident rate, most consistent SLA compliance.

---

## Repository Contents

```
├── README.md
├── hub-content.html                     — live interactive dashboard
├── architecture diagram.png             — full solution architecture
├── operations_daily.csv                 — 6,564 daily ops records
├── maintenance_work_orders.csv          — 7,761 work orders
├── finance_monthly.csv                  — 864 budget vs. actual records
├── assets.csv                           — 540 assets, condition + lifecycle
├── customer_experience_monthly.csv      — CSAT and NPS by site and month
├── installed_customer_base_monthly.csv  — customer and cabinet counts
├── site_dim.csv                         — 12 sites, metadata and capacity
├── date_dim.csv                         — 547 dates, time intelligence
├── data_dictionary.csv                  — 105 fields documented
└── table_summary.csv                    — row counts and column inventory
```

---

## How I Built It

I started with the business questions — what decisions does a site operations leader actually need to make? — and worked backward from there to determine what data was needed, at what grain, and in what structure.

The star schema was deliberate. A flat table would have been faster but harder to extend. A properly modeled schema means anyone can add a data source and have it filter across every existing view without touching existing logic.

The insight layer came last. Once the visuals were built, I wrote the "so what" for each finding — structured as a recommendation a director could act on, not just a caption under a chart.

---

## Skills Demonstrated

| Area | Details |
|---|---|
| Data Engineering | Python · pandas · data validation · schema design |
| Database | SQL · MySQL · star schema · dimensional modeling |
| Analytics & BI | Power BI · DAX · time intelligence · KPI framework design |
| Visualization | Multi-view dashboard · drill-through · cross-filter |
| Communication | Insight narrative · stakeholder reporting · access hub design |
| Domain | Asset lifecycle · SLA management · CSAT/NPS · OpEx/CapEx |

---

## About Me

I'm Padmasree (Padma) Sappa — Senior Business Analyst with 6+ years across analytics, operations, and delivery.

At **Amazon** I built reporting pipelines and automation that cut manual hours by 1,200+ annually and improved decision accuracy by 28%. At **CGI** I led delivery analytics for a global Agile program, improving sprint predictability by 30%. MS in Business Analytics, SFSU (GPA 3.97). Certified Scrum Master and Product Owner.

Open to roles in analytics, reporting, and business intelligence — especially where the work involves building something sustainable, not just one more report.

📧 sdnps7196@gmail.com &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/padmasreesappa/) &nbsp;·&nbsp; [Portfolio](https://dsappa7196-github-io-yjma.vercel.app/)

---

*Built with care, and a belief that good analytics should answer questions — not just display numbers.*
