# Career Intelligence Platform

> **The Career Intelligence Platform** is a cloud-native, modular data engineering platform for ingesting, profiling, transforming and analysing recruitment data. It is designed to standardise heterogeneous recruitment datasets into a common **Career Intelligence document model**, enabling workforce analytics, labour market intelligence and future AI-powered applications.
>
> The NHS Jobs dataset is used as the initial implementation to validate the platform architecture. The platform itself is intentionally dataset-agnostic and designed to support additional recruitment providers with minimal code changes.

---

## Table of Contents

<details>
<summary>Click to expand</summary>

- [Project Summary](#project-summary)
- [Business Problem](#business-problem)
- [Proposed Solution](#proposed-solution)
- [Key Features](#key-features)
- [Business Benefits](#business-benefits)
- [System Architecture](#system-architecture)
- [Architecture Principles](#architecture-principles)
- [High-Level Architecture](#high-level-architecture)
- [Component Responsibilities](#component-responsibilities)
- [Technology Stack](#technology-stack)
- [Canonical Data Model](#canonical-data-model)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [AI Roadmap](#ai-roadmap)
- [Installation & Setup](#installation--setup)
- [Future Improvements](#future-improvements)
- [Conclusion](#conclusion)

</details>

---

## Project Summary

Recruitment data is valuable not only to job seekers but also to organisations analysing workforce demand, regional skills shortages, salary trends and labour market activity.

The Career Intelligence Platform provides a reusable cloud-native ETL architecture that ingests recruitment datasets, profiles their structure, cleans and validates the data, and maps every source into a common canonical document model.

Once standardised, the data can be analysed consistently regardless of its original source and provides a foundation for semantic search, AI enrichment and workforce analytics.

---

## Business Problem

Organisations wishing to analyse recruitment trends often spend significant effort cleaning and standardising data before meaningful analysis can begin.

Common challenges include:

- Different schemas between recruitment providers
- Inconsistent salary and location formats
- Missing or incomplete values
- Bespoke ETL pipelines for every new dataset

These issues increase development effort and make labour market analysis difficult.

---

## Proposed Solution

The platform separates:

- Extraction
- Profiling
- Cleaning
- Canonical Mapping
- Validation
- Storage
- AI Enrichment

Every recruitment dataset is transformed into a common Career Intelligence document, enabling consistent analytics across multiple sources.

---

## Key Features

- Cloud-native modular ETL architecture
- Canonical Career Intelligence document model
- Amazon S3 data lake
- Databricks (Apache Spark)
- MongoDB document storage
- Configuration-driven processing
- Reusable mapping architecture
- AI-ready document schema
- Designed for semantic search and RAG

---

## Business Benefits

- Reusable ETL platform
- Reduced integration effort
- Consistent analytics
- Separation of configuration, schema and mapping logic
- Foundation for AI-assisted mapping

---
# System Architecture

## Architecture Principles

- Modular Python architecture
- Separation of ETL stages
- Separation of configuration, schema and mapping
- Cloud-first design
- Extensible canonical data model
- AI-ready architecture


## High-Level Architecture

*(Insert architecture diagram)*

```
Raw Data
    │
    ▼
 Amazon S3
    │
    ▼
Databricks
    │
 ┌──┴───────────┐
 ▼              ▼
MongoDB      Analytics
```

---

## Component Responsibilities

### Amazon S3

...

### Databricks

...

### MongoDB

...

### EC2

...

### SQL Server (Optional)

...

---


---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Python | ETL & Orchestration |
| Amazon S3 | Data Lake |
| Databricks | Processing |
| MongoDB | Document Store |
| EC2 | Hosting |
| SQL | Analytics |
| GitHub | Version Control |

---

## Canonical Data Model

```
job
organisation
employment
location
dates
metadata
ai
```

---

# Project Structure

```text
Career-Intelligence-Platform/
│
├── .env
├── .env.example
├── .gitignore
├── app.py
├── config.py
├── README.md
├── requirements.txt
├── assets/
│   └── schema.md
├── data/
│   ├── exports/
│   ├── processed/
│   └── raw/
│       ├── jobs_raw.csv
│       └── nhs-jobs-metadata.json
├── docs/
├── images/
├── logs/
├── notebooks/
├── src/
│   ├── analytics/
│   ├── clean/
│   │   └── clean.py
│   ├── database/
│   │   └── csv_loader.py
│   ├── extract/
│   ├── load/
│   ├── models/
│   │   └── career_document.py
│   ├── profile/
│   │   └── reports.py
│   ├── transform/
│   │   └── mapper.py
│   └── utils/
├── tests/
└── .venv/
```

---

# Data Model

### Document Schemas

**MongoDB Collection structure**

jobs
│
├── job
│   ├── title
│   ├── reference
│   ├── description
│   └── specialty
│
├── organisation
│   ├── name
│   ├── department
│   └── postcode
│
├── employment
│   ├── type
│   ├── working_pattern
│   ├── salary
│   └── pay_band
│
├── location
│   ├── town
│   ├── postcode
│   ├── latitude
│   └── longitude
│
├── dates
│
├── metadata
│
└── ai

---


## AI Roadmap

- AI-assisted schema detection
- Intelligent field mapping
- Automatic mapping configuration
- Skill extraction
- Semantic search
- Career recommendation engine

---

# Installation & Setup

Clone repository

Install requirements

Configure AWS

Configure MongoDB

Run pipeline

---

## Future Improvements

- Additional recruitment providers
- Live API ingestion
- Incremental ETL
- Vector database
- Dashboards
- CI/CD
- LLM-powered career intelligence assistant

---

## Conclusion

The Career Intelligence Platform demonstrates how a reusable cloud-native data engineering architecture can standardise heterogeneous recruitment datasets into a common Career Intelligence model.

By separating configuration, schema and mapping logic, the platform can be adapted to new recruitment sources with minimal code changes while providing a scalable foundation for analytics and AI-powered career intelligence.
