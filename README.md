# Workflow Automation Builder

## Project Overview

This project implements an AI Workflow Builder using React, ReactFlow, and FastAPI.

### Features

 Reusable BaseNode abstraction
 9 workflow node types
 Dynamic Text Node resizing
 Variable parsing using {{variable}}
 Dynamic handle generation
 DAG validation
 Frontend ↔ Backend integration
 Pipeline analysis modal

---

## Tech Stack

### Frontend

 React
 ReactFlow
 JavaScript

### Backend

 FastAPI
 Pydantic
 Uvicorn

---

## Running the Project

### Backend

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
python -m uvicorn main:app --reload
```

Backend URL:

```txt
http://localhost:8000
```

---

### Frontend

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start application:

```bash
npm start
```

Frontend URL:

```txt
http://localhost:3000
```

---

## Pipeline Analysis

The backend returns:

```json
{
  "num_nodes": int,
  "num_edges": int,
  "is_dag": bool
}
```

The frontend displays the results in a modal after submission.
