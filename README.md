# Healthcare Patient Data Management System

> **Portfolio Note**: Portfolio recreation of HIPAA-compliant system built at Omfys Technologies.

## 🎯 Overview
HIPAA-compliant patient data management consolidating records from multiple hospitals using Airflow, PostgreSQL, OAuth2.0, Elasticsearch, managing **500K+ patient records**.

## 📊 Key Metrics
- **Records**: 500K+ patients
- **Availability**: 99.95%
- **Search Latency**: <1s
- **Compliance**: HIPAA, SOC 2

## 🛠️ Tech Stack
- **API**: FastAPI, OAuth2.0, JWT
- **ETL**: Apache Airflow
- **Storage**: PostgreSQL (AES-256 encryption)
- **Search**: Elasticsearch
- **API Gateway**: Kong
- **BI**: Power BI

## ⚡ Key Features

### 1. HIPAA Compliance
- Field-level AES-256 encryption for PHI
- OAuth2.0 authorization flows
- JWT token validation
- Audit logging of all access
- Row-level security

### 2. Secure API Gateway
- Kong Gateway with rate limiting (100 req/min)
- API versioning
- JWT validation
- TLS/SSL encryption

### 3. Full-Text Patient Search
- Elasticsearch with custom analyzers
- Fuzzy matching and phonetic search
- Sub-second response times
- Handles 500K+ records

### 4. Automated ETL Pipelines
- Airflow orchestration
- Integration with multiple EHR systems
- Data quality checks
- Incremental loading

## 📁 Project Structure
```
healthcare-data-system/
├── src/
│   ├── api/                 # FastAPI with OAuth2
│   ├── database/            # Encrypted PostgreSQL
│   └── search/              # Elasticsearch
├── airflow/dags/            # ETL pipelines
├── kong/kong.yml            # API Gateway config
└── README.md
```

## 🚀 Getting Started

```bash
git clone https://github.com/Amanroy666/healthcare-data-system.git
cd healthcare-data-system
pip install -r requirements.txt
docker-compose up -d
```

## 🔒 Security Features
- Field-level encryption (AES-256)
- OAuth2.0 + JWT authentication
- Rate limiting
- Audit logging
- HIPAA compliance

## 👤 Author

**Aman Roy** - Data Engineer at Omfys Technologies  
📧 contactaman000@gmail.com | 💼 [LinkedIn](https://linkedin.com/in/amanxroy)
