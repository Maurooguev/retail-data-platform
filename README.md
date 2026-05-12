# Retail Data Platform

End-to-end retail and supply chain data engineering project built with Python, PostgreSQL, Docker and Metabase.

---

# Project Overview

This project simulates a retail company's data platform.

The pipeline generates fake sales, customer, inventory and warehouse data, stores it in PostgreSQL and visualizes business KPIs using Metabase dashboards.

---

# Tech Stack

- Python
- PostgreSQL
- Docker
- Metabase
- SQL
- Git & GitHub

---

# Architecture

```text
Python ETL Pipeline
        ↓
PostgreSQL Database
        ↓
Metabase Dashboards
```

---

# Features

- Modular ETL pipeline
- Fake retail and supply chain data generation
- PostgreSQL relational database
- Automated sales batch generation
- KPI dashboards
- Dockerized infrastructure
- Git version control

---

# Project Structure

```text
retail-data-platform/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── generate_data.py
│   ├── generate_sales_batch.py
│   └── scheduler.py
│
├── sql/
│   └── schema.sql
│
├── docker-compose.yml
├── requirements.txt
├── COMMANDS.txt
└── README.md
```

---

# Setup

## Clone repository

```bash
git clone https://github.com/Maurooguev/retail-data-platform.git
```

---

## Start Docker containers

```bash
docker compose up -d
```

---

## Install Python dependencies

```bash
pip install -r requirements.txt
```

---

# Run Full ETL Pipeline

```bash
python scripts/generate_data.py
```

---

# Generate Incremental Sales Batch

```bash
python scripts/generate_sales_batch.py
```

---

# Open Metabase

```text
http://localhost:3000
```

---

# Future Improvements

- Apache Airflow orchestration
- Cloud deployment
- Real-time streaming
- Data warehouse layer
- Advanced analytics dashboards
- CI/CD pipelines

---

# Author

Mauro Guevara