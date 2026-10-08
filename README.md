# AI Coding Agent

## Overview

AI Coding Agent that analyzes a code repository, understands a developer request, identifies relevant files, generates code modifications, creates diffs, and explains changes.

---

## Features

- Natural language coding requests
- Repository analysis
- Relevant file selection
- Plan generation
- Code modification
- Diff generation
- Change explanation
- Download modified repository

---

## AI Safety & Validation

Implemented:

- Prompt Injection Detection
- File Access Restrictions
- Python Syntax Validation
- Automated Evaluation Metrics

---

## Evaluation

File selection quality is evaluated using:

- Precision
- Recall
- F1 Score

Example Results:

| Task | Precision | Recall | F1 |
|--------|--------|--------|--------|
| Add username validation | 0.33 | 1.0 | 0.5 |
| Write tests | 1.0 | 1.0 | 1.0 |

---

## Architecture

User Task
↓
Streamlit UI
↓
Repository Loader
↓
File Selector
↓
Planner
↓
Code Modifier
↓
Diff Generator
↓
Explanation Generator
↓
Result Download

---

## Run Locally

### Clone

git clone <repo-url>

### Install

pip install -r requirements.txt

### Configure

Create .env

GROQ_API_KEY=your_key

### Run

streamlit run app.py

---

## Deployment

Streamlit Cloud

---

## Author

Vaibhav Anil Chitade