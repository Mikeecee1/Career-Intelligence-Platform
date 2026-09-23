#  Career Intelligence Platform

> The Career Intelligence Platform is a cloud-native, modular data engineering platform for ingesting, profiling, transforming and analysing recruitment data. The platform is designed to support multiple recruitment datasets through a reusable ETL architecture. [The NHS Jobs dataset](https://www.kaggle.com/datasets/homelesssandwich/nhs-jobs?resource=download) is used as the initial implementation to validate the design.



---

## Table of Contents

<details>
<summary>Click to expand</summary>

- [Project Status](#project-status)
- [Key Features](#key-features)
- [Business Scenario](#business-scenario)
- [Overview](#overview)
- [Business Problem](#business-problem)
- [Project Objectives](#project-objectives)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Technology Choices](#technology-choices)
- [Architecture Principles](#architecture-principles)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Data Flow](#data-flow)
- [ETL Pipeline](#etl-pipeline)
- [Data Processing](#data-processing)
- [Analytics & Insights](#analytics--insights)
- [Cloud Infrastructure](#cloud-infrastructure)
- [Future AI Enhancements](#future-ai-enhancements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Roadmap](#project-roadmap)
- [Risks & Assumptions](#risks--assumptions)
- [Lessons Learned](#lessons-learned)
- [Future Improvements](#future-improvements)
- [References](#references)

</details>

---

## Project Status

| Stage | Status |
|--------|:------:|
| Project Design | ✅ Complete |
| Environment Setup | ✅ Complete |
| Data Ingestion | 🔄 In Progress |
| ETL Pipeline | ⏳ Planned |
| MongoDB Integration | ⏳ Planned |
| Analytics | ⏳ Planned |
| Semantic Search | 🚀 Future Enhancement |

---

## Key Features

- Cloud-native ETL pipeline
- Amazon S3 Data Lake
- Databricks (Apache Spark) data processing
- MongoDB document database hosted on EC2
- Python data engineering workflows
- SQL analytics
- Skill extraction from job descriptions
- Career intelligence reporting
- Designed for future Semantic Search and RAG

---

## Business Scenario

NHS organisations publish thousands of job vacancies containing valuable information about skills, career progression and recruitment trends. However, this information is spread across individual job adverts, making large-scale analysis difficult.

The NHS Career Intelligence Platform provides a modern cloud-based data platform that ingests, transforms and enriches NHS recruitment data. The platform enables workforce analytics today while laying the foundations for AI-powered career guidance through semantic search and Retrieval-Augmented Generation (RAG).

---

# Overview

## Project Summary

*(Brief overview of the project.)*

---

# Business Problem

## Background

Why does this project exist?

Who would benefit?

What problem is being solved?

---

## Proposed Solution

High level description of the platform.

---

# Project Objectives

### Primary Objectives

- [ ]
- [ ]
- [ ]

### Secondary Objectives

- [ ]
- [ ]
- [ ]

---

# System Architecture

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

# Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Language | Python | ETL |
| Database | MongoDB | Document storage |
| Cloud Storage | AWS S3 | Data lake |
| Compute | Databricks | Data processing |
| Hosting | EC2 | MongoDB server |
| Analytics | SQL Server | Reporting |
| Version Control | GitHub | Source control |

---

# Technology Choices

| Decision | Rationale |
|----------|-----------|
| MongoDB | Flexible document structure for rich job adverts and future embeddings |
| Amazon S3 | Data lake for raw and processed datasets |
| Databricks | Distributed ETL and feature engineering using Spark |
| EC2 | Self-managed MongoDB deployment and cloud infrastructure experience |
| SQL Server | Structured reporting and analytical queries |
| Python | Primary ETL and orchestration language |

---

# Architecture Principles

The platform has been designed around several core principles:

- Separation of extraction, transformation and loading stages
- Configuration-driven deployment
- Modular Python architecture
- Cloud-first design
- Reproducible data processing
- Extensible document model
- Future support for AI workloads

---

# Data Sources

## Primary Dataset

Description

Fields

Size

Licence

---

## Supporting Datasets

| Dataset | Purpose |
|----------|----------|
| NHS Band Information | |
| Organisation Information | |
| Region Lookup | |

---

# Project Structure

```text
NHS-Career-Intelligence/
│
├── .venv/
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
├── docs/
├── images/
├── notebooks/
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── database/
│   ├── analytics/
│   └── utils/
├── tests/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── app.py
└── config.py
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

## MongoDB Collections

### Jobs

Description

Example document

---

### Skills

Description

---

### Organisations

Description

---

### Metadata

Description

---

# Data Flow

---

# ETL Pipeline

## Extract

Where does the data come from?

---

## Transform

Cleaning

Validation

Normalisation

Feature Engineering

Skill Extraction

---

## Load

MongoDB

S3 Processed Zone

Analytics datasets

---

# Data Processing

## Data Cleaning

- Remove duplicates
- Handle missing values
- Standardise dates
- Standardise salaries

---

## Feature Engineering

Examples

- Salary ranges
- NHS Band extraction
- Skill extraction
- Location standardisation

---

# Analytics & Insights

## Example Questions

- Which technical skills are most requested?
- Which NHS Bands offer the highest salaries?
- Which regions have the most vacancies?
- What skills appear together most often?

---

## Example Dashboards

*(Screenshots later)*

---

# Cloud Infrastructure

## AWS Architecture

*(Diagram)*

---

## S3 Data Lake

```text
raw/

processed/

analytics/

exports/
```

---

## MongoDB Deployment

EC2 instance

Collections

Indexes

---

# Future AI Enhancements

## Semantic Search

Describe how embeddings could be added.

---

## Retrieval-Augmented Generation (RAG)

Potential architecture.

---

## Career Recommendation Engine

Future roadmap.

---

# Installation & Setup

Clone repository

Install requirements

Configure AWS

Configure MongoDB

Run pipeline

---

# Usage

Example workflow.

---

# Project Roadmap

## Phase 1

Cloud ETL

## Phase 2

Analytics

## Phase 3

Semantic Search

## Phase 4

RAG

---

# Risks & Assumptions

## Assumptions

- NHS dataset remains publicly available.
- AWS Free Tier resources are sufficient.
- Databricks Community Edition provides adequate processing capacity.

## Risks

- Dataset schema changes.
- Missing salary information.
- Inconsistent job descriptions.
- Large datasets may require optimisation.

---

# Lessons Learned

Challenges encountered.

Solutions implemented.

---

# Future Improvements

- Live NHS API integration
- Incremental ETL
- Vector database
- LLM-powered career assistant
- Dashboard
- CI/CD pipeline

---

# References

Datasets

Documentation

AWS

MongoDB

Databricks

NHS Jobs

GitHub
