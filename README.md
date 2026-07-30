# Career Intelligence Platform

> **The Career Intelligence Platform** is a cloud-native, modular data engineering platform for ingesting, profiling, transforming and analysing recruitment data. It is designed to standardise heterogeneous recruitment datasets into a common **Career Intelligence document model**, enabling workforce analytics, labour market intelligence and future AI-powered applications.
>
> The NHS Jobs dataset is used as the initial implementation to validate the platform architecture. The platform itself is intentionally dataset-agnostic and designed to support additional recruitment providers with minimal code changes.

---

## Table of Contents

<details>
<summary>Click to expand</summary>

- [Project Summary](#project-summary)
- [Design Philosophy](#design-philosophy)
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

## Design Philosophy

The Career Intelligence Platform is designed around the principle of separating business logic from source-specific implementation.

Rather than building bespoke ETL pipelines for individual recruitment datasets, the platform standardises all data into a common Career Intelligence document model. This approach allows new data sources to be integrated primarily through configuration and mapping rather than changes to application code.

As the platform evolves, AI-assisted schema discovery and an expanding alias library will further reduce the effort required to onboard new recruitment providers while maintaining a consistent analytical model.

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

The Career Intelligence Platform provides organisations with a reusable and scalable framework for integrating recruitment data from multiple providers into a common data model. By separating extraction, transformation, mapping and persistence, the platform significantly reduces the effort required to onboard new recruitment datasets.

Unlike bespoke ETL solutions designed for a single source, the platform is intended to become increasingly valuable over time as additional providers, mapping configurations and AI-assisted schema discovery are incorporated.

Key business benefits include:

- Reduced development effort when integrating new recruitment datasets
- Consistent analytics across heterogeneous data sources
- Reusable canonical document model for downstream applications
- Simplified maintenance through separation of configuration and application logic
- Foundation for semantic search, AI enrichment and labour market intelligence

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

                    Recruitment Data Sources
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
          CSV Files                        Future APIs
             │                                   │
             └───────────────┬───────────────────┘
                             ▼
                      Career Intelligence Platform
                             │
      ┌──────────┬───────────┬────────────┬────────────┐
      ▼          ▼           ▼            ▼
   Profile     Clean       Map       Validate
                             │
                             ▼
                 Career Intelligence Document
                             │
                             ▼
                         MongoDB
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
           Analytics             AI Applications

---


## Component Responsibilities

### Data Extraction

Responsible for loading recruitment datasets from external sources. The current implementation supports CSV ingestion, with the architecture designed to accommodate APIs and additional file formats in future.

---

### Data Profiling

Generates summary statistics describing the incoming dataset, including missing values, duplicate records and data types. Profiling informs the cleaning process and provides transparency over data quality.

---

### Data Cleaning

Applies configurable data quality rules including duplicate removal, date conversion, column standardisation and salary normalisation. Cleaning behaviour is controlled through configuration to simplify future extension.

---

### Canonical Mapping

Transforms heterogeneous recruitment datasets into a common Career Intelligence document model. This abstraction layer separates source-specific schemas from downstream analytics.

---

### Validation

Verifies that each generated Career Intelligence document conforms to the canonical schema before persistence. Validation provides early detection of mapping errors and incomplete data.

---

### MongoDB Repository

Stores validated Career Intelligence documents using a hierarchical document structure that naturally represents recruitment data while remaining independent of the original source schema.

---

### Future AI Services

Future development will introduce AI-assisted schema mapping, semantic search, skills extraction and career recommendation services built on top of the canonical document model.


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

The Career Intelligence Platform stores every recruitment record using a common document schema regardless of the original data source.

The current canonical document consists of the following logical sections:

- **job** – Vacancy information, identifiers and descriptions
- **organisation** – Employer and organisational information
- **employment** – Contract, salary and working pattern
- **location** – Geographic information
- **dates** – Publication and closing dates
- **metadata** – Dataset provenance and ingestion information
- **ai** – Reserved for future AI enrichment including skills, embeddings and semantic metadata

This stable schema allows downstream analytics and AI applications to remain independent of individual recruitment providers.

---

# Project Structure

```text
Career-Intelligence-Platform/
│
├── .env
├── .env.example
├── .gitignore
├── app.py
├── README.md
├── README_old.md
├── requirements.txt
├── notes.md
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
│   ├── config.py
│   ├── database/
│   │   ├── connection.py
│   │   ├── query.py
│   │   └── repository.py
│   ├── extract/
│   │   └── csv_loader.py
│   ├── load/
│   ├── models/
│   │   └── career_document.py
│   ├── profile/
│   │   └── reports.py
│   ├── transform/
│   │   └── mapper.py
│   ├── utils/
│   └── validation/
│       └── validator.py
├── tests/
│   ├── test_connection.py
│   ├── test_repository.py
│   └── test_repository_2.py
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

## Installation & Setup

1. Clone the repository

2. Create a Python virtual environment

3. Install project dependencies

```bash
pip install -r requirements.txt
```

4. Configure environment variables

Create a `.env` file containing:

```
MONGO_URI=
MONGO_DATABASE=
MONGO_COLLECTION=
```

5. Place the NHS Jobs dataset into:

```
data/raw/
```
(repeat for similar datasets)

6. Run the application

```bash
python app.py
```

The platform will profile, clean, transform, validate and store Career Intelligence documents within MongoDB.

---

## Future Improvements

## Future Improvements

The current implementation demonstrates the core architecture using the NHS Jobs dataset. Future development will focus on extending the platform into a generic recruitment data integration framework.

Planned enhancements include:

- Support for additional recruitment providers
- API-based ingestion
- Configuration-driven schema mappings
- AI-assisted schema discovery
- Growing alias library for automatic field recognition
- Duplicate detection across multiple recruitment providers
- Semantic search using vector embeddings
- Skills extraction using Large Language Models
- Databricks processing pipeline
- Automated cloud deployment
- Interactive analytics dashboard
---

## Conclusion

The Career Intelligence Platform demonstrates how a reusable cloud-native data engineering architecture can standardise heterogeneous recruitment datasets into a common Career Intelligence model.

By separating configuration, schema and mapping logic, the platform can be adapted to new recruitment sources with minimal code changes while providing a scalable foundation for analytics and AI-powered career intelligence.
