# Regulatory Relevancy

A document intelligence system for **regulatory document relevancy detection**. The project leverages Natural Language Processing (NLP) and Machine Learning techniques to identify and retrieve the most relevant sections from large regulatory documents, enabling faster compliance analysis and information retrieval.

---

## Overview

Regulatory documents are often lengthy, complex, and difficult to navigate. This project provides an AI-powered solution for analyzing regulatory documents and determining the relevance of specific sections based on user queries or predefined criteria.

The project is structured into three major components:

- **AI Module** – Machine learning and document processing pipeline.
- **Backend** – APIs and business logic for serving predictions.
- **Frontend** – User interface for interacting with the system.

---

## Features

- Intelligent regulatory document analysis
- Relevant document/section retrieval
- AI-powered document processing pipeline
- Modular architecture separating AI, backend, and frontend
- Easy integration with larger compliance platforms
- Support for processing XML regulatory documents

---

## Project Architecture

```text
regulatory-relevancy/
│
├── AI/                         # AI models and document processing
│   ├── __init__.py
│   ├── sor_app.py              # Main AI inference application
│   └── usa/
│       ├── 12.xml              # Regulatory document
│       ├── 17.xml              # Regulatory document
│       └── 47.xml              # Regulatory document
│
├── backend/                    # Backend services and APIs
│   ├── __init__.py
│
├── frontend/                   # Frontend application
│   ├── __init__.py
│
├── requirements.txt            # Python dependencies
├── LICENSE
├── README.md
└── __init__.py
```

---

## Requirements

- Python 3.8+
- pip
- Virtual Environment (recommended)

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/haider-ali-77/document-regulatory-relevency.git
```

Move into the project directory

```bash
cd document-regulatory-relevency
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Navigate to the AI module

```bash
cd AI
```

Run the application

```bash
python sor_app.py
```

The application will process the regulatory documents located in

```text
AI/usa/
```

and perform document relevancy analysis.

---

## Project Workflow

```text
Regulatory XML Documents
            │
            ▼
      Document Parsing
            │
            ▼
      NLP Preprocessing
            │
            ▼
   Relevancy Prediction
            │
            ▼
 Relevant Document Retrieval
            │
            ▼
     Backend / Frontend
```

---

## Directory Description

| Directory | Description |
|-----------|-------------|
| **AI/** | Contains the AI models, document processing pipeline, and inference scripts. |
| **AI/usa/** | Regulatory XML documents used for processing and evaluation. |
| **backend/** | Backend services and APIs for model integration. |
| **frontend/** | User interface for interacting with the system. |
| **requirements.txt** | Python package dependencies. |

---

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Machine Learning
- XML Processing
- Document Intelligence

---

## Future Improvements

- REST API integration
- Web-based dashboard
- Support for additional regulatory datasets
- Semantic search using transformer-based embeddings
- Vector database integration
- Large Language Model (LLM) assisted document retrieval
- Explainable AI for relevance scoring

---

## License

This project is licensed under the MIT License. See the **LICENSE** file for details.

---

## Author

**Haider Ali**

Machine Learning Engineer | Computer Vision | NLP | Document Intelligence

GitHub: https://github.com/haider-ali-77