# DIU Admission Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot designed to answer admission-related questions using information extracted from university documents. The system allows administrators to upload admission PDFs, generate embeddings, and provide context-aware responses through a Large Language Model (LLM).

---

## Overview

The chatbot uses a RAG pipeline to ensure responses are generated from the uploaded admission document rather than relying solely on the model's general knowledge.

When a user asks a question:

1. The query is received by the FastAPI backend.
2. Common predefined queries (e.g., greetings) are handled directly.
3. For admission-related questions, the system searches the FAISS vector database for relevant information.
4. Retrieved context is injected into a prompt template.
5. The LLM generates an answer based only on the retrieved context.
6. The response is returned to the user.

## System Architecture

![alt text](<Rag Architecture.png>)


```text
User Question
      │
      ▼
 FastAPI Route
      │
      ▼
 Common Query Check
      │
      ├── Match Found
      │       ▼
      │   Direct Response
      │
      └── No Match
              ▼
          RAG Chain
              │
              ▼
        FAISS Retriever
              │
              ▼
      Relevant Context
              │
              ▼
       Prompt Template
              │
              ▼
         GPT-4o Mini
              │
              ▼
        Generated Answer
```

---

## Project Structure

```text
app/
│
├── data/
│   ├── rag.pdf
│   └── faiss_index/
│
├── model/
│   └── models.py
│
├── prompts/
│   └── prompts.py
│
├── rag/
│   ├── ingest.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── chain.py
│
├── routes/
│   ├── admin.py
│   └── routes.py
│
├── service/
│   ├── chat_service.py
│   └── common_query.py
│
├── static/
├── template/
└── main.py
```

---

## Component Responsibilities

### `ingest.py`

Responsible for creating the knowledge base.

* Loads the uploaded PDF
* Generates embeddings
* Creates a FAISS vector database
* Stores the vector index locally

### `vector_store.py`

Handles loading the saved FAISS index whenever retrieval is required.

### `retriever.py`

Searches the vector database and returns the most relevant document chunks for a user query.

### `prompts.py`

Contains the prompt template used to instruct the LLM.

### `chain.py`

Defines the LangChain LCEL RAG pipeline:

```text
Retriever
   ↓
Prompt
   ↓
LLM
   ↓
Output Parser
```

### `chat_service.py`

Acts as the service layer that executes the RAG chain and returns responses.

### `routes.py`

Handles chatbot API requests.

### `admin.py`

Provides administrative functionality:

* Upload PDF
* Rebuild vector database
* View current PDF

---

## Technologies Used

* FastAPI
* LangChain (LCEL)
* OpenAI Embeddings
* GPT-4o Mini
* FAISS
* HTML
* CSS
* JavaScript

---

## Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=your_base_url
```

### Run Application

```bash
uvicorn app.main:app --reload
```

---

## Usage

### Chat Interface

```text
http://localhost:8000
```

### Admin Panel

```text
http://localhost:8000/admin
```

Admin users can:

1. Upload a PDF knowledge source
2. Rebuild the vector database
3. Verify the uploaded document

---

## Future Improvements

* Document chunking
* Retrieval reranking
* Source citations
* Chat history and memory
* Streaming responses
* Multi-document support
* Hybrid search

---
