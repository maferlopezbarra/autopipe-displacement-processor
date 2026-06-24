
# AutoPIPE Imposed Displacements Processor

A Python-based **ETL + API tool** to process AutoPIPE structural data using SQLite, compute seismic displacements, export results to CSV, and expose the pipeline via a FastAPI service.

---

## Overview

This project implements a complete data pipeline for structural engineering automation:

- Extracts support data from a SQLite database (AutoPIPE format)
- Processes vertical coordinates to compute seismic drift values
- Generates formatted CSV output compatible with AutoPIPE
- Exposes the same pipeline via a REST API using FastAPI
- Includes unit tests for core components

---

## Tech Stack

- Python
- SQLite
- FastAPI
- Pytest
- CSV processing
  
---

## Project Structure
project/
│
├── src/
│   ├── main.py                       # CLI Entry point
│   ├── api.py                        # FastAPI application
│   ├── database.py                   # CLI configuration
│   ├── extractors.py                 # SQLite queries
│   ├── processors.py                 # Engineering calculations
│   ├── writers.py                    # CSV output generation
│   └── services/
│       └── displacement_service.py   # API business logic
├── tests/
│   ├── test_extractors.py
│   ├── test_processors.py
│   └── test_writers.py
│
├── data/
│   ├── input/                        # Input database files
│   └── output/                       # Generated CSV files
│
└── README.md

---

## Installation

Create enviroment:

```bash
python -m venv .venv
```
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

### Run CLI pipeline

From the project root:

```bash
python -m src.main
```

### Custom parameters
```bash
python -m src.main --db my_database.db --elevation 10300 --factor 250
```
- The database must be located in: data/input/

### Output
data/output/output.csv

---

## Run API
Start server:

```bach
uvicorn src.api:app --reload
```
API documentation:
- http://127.0.0.1:8000/docs

Endpoint:
GET /displacements

Example:
/displacements?db=input.db&elevation=10300&factor=250

---

## Testing
Run:

```bach
pytest
```

## Engineering Logic
Drift calculation:

```Python
drift = ceil((Z - elevation) / factor)
```
Negative drift values are set to zero.

## Purpose
This project demonstrates:
- Python backend development
- ETL pipeline design
- SQL data extraction
- API development
- Automated testing

## Autor
Maria Fernanda Lopez Barra

