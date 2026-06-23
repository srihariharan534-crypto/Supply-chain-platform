# Supply Chain Platform Architecture

## Overview
The platform uses a layered architecture to ingest, process, analyze, and present supply chain data.

## Data Layer
- **Raw Data (`data/raw/`)**: Synthetic datasets generated using Faker.
- **ETL Pipeline (`etl/`)**: Scripts for extracting CSVs, transforming data (cleaning, standardizing), validating, and loading into the warehouse.
- **Data Warehouse (`data/warehouse/`)**: SQLite database with a Star Schema.
- **Schema (`schema/`)**: SQL definitions for tables, views, and indexes.

## Analytics & Intelligence Layer
- **Feature Store (`data/feature_store/`)**: Feature engineering modules for ML.
- **Intelligence Modules (`analytics/`)**: Business logic for KPIs, scorecards, and analysis.
- **Models (`models/`)**: ML models for forecasting and anomaly detection using scikit-learn.

## Decision Support Layer
- **Decision Support (`analytics/decision_support.py`)**: Recommendation and Alert engines.
- **KPI Engine (`executive_kpis/kpi_engine.py`)**: Computes all configured metrics.

## Presentation Layer
- **API (`api/`)**: FastAPI endpoints to expose insights.
- **UI (`app.py`)**: Streamlit application rendering Control Towers and Dashboards.
