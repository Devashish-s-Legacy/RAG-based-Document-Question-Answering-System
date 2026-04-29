RAG-based-Document-Question-Answering-System
A full-stack AI application that enables users to upload documents (PDFs) and ask natural language questions. The system uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers based on document content.

Features
Upload and process multiple PDF documents
Semantic search using vector embeddings
Context-aware answer generation using LLMs
FastAPI backend with modular architecture
Interactive frontend (Streamlit / React)
Evaluation endpoint for response analysis
Prompt engineering to reduce hallucinations
Logging, error handling, and validation

How It Works
User Query
   ↓
Retriever (ChromaDB + Embeddings)
   ↓
Relevant Document Chunks
   ↓
LLM (Generation)
   ↓
Final Answer

The system uses RAG (Retrieval-Augmented Generation):

Retrieves relevant document chunks using semantic similarity
Injects them into the prompt
Generates grounded responses using an LLM

Architecture
Frontend (Streamlit / React)
        ↓
FastAPI Backend
        ↓
Service Layer
        ↓
RAG Pipeline
   ├── Retrieval (ChromaDB)
   └── Generation (LLM)

Tech Stack
Backend: FastAPI
Frontend: Streamlit / React
AI Framework: LangChain
Vector Database: ChromaDB
Embeddings: HuggingFace (all-MiniLM-L6-v2)
LLM: OpenAI / Gemini / Local (Ollama)
Language: Python

Project Structure
app/
 ├── main.py
 ├── api/
 │    ├── routes.py
 │    ├── upload_routes.py
 │    └── eval_routes.py
 │
 ├── services/
 │    └── rag_service.py
 │
 ├── rag/
 │    ├── ingest.py
 │    ├── retrieve.py
 │    └── generate.py
 │
 ├── utils/
 │    └── logger.py

frontend/
 └── app.py

data/
 └── documents/

db/

Setup Instructions

1. Clone Repository
git clone <your-repo-url>
cd <project-folder>
2. Install Dependencies
pip install -r requirements.txt
3. Run Backend
uvicorn app.main:app --reload
4. Run Frontend
streamlit run app/frontend/app.py
| Endpoint  | Method | Description                  |
| --------- | ------ | ---------------------------- |
| `/ask`    | POST   | Ask questions from documents |
| `/upload` | POST   | Upload and index PDF         |
| `/eval`   | GET    | Evaluate system responses    |
| `/health` | GET    | Check API status             |

Example Request
POST /ask
{
  "query": "What is this document about?"
}

Example Response
{
  "question": "What is this document about?",
  "answer": "...",
  "sources": [...],
  "confidence": 0.8
}

Key Concepts
Retrieval-Augmented Generation (RAG)
Semantic Search & Vector Embeddings
Prompt Engineering
LLM Integration
Modular Backend Design

Future Improvements
Add chat memory (conversation context)
Implement hybrid search (BM25 + vector)
Add reranking for better retrieval
Deploy using Docker + cloud (Render/AWS)
Improve UI with full React frontend

Motivation

Traditional LLMs rely only on pretrained knowledge.
This system enhances accuracy by grounding responses in user-provided documents, making it more reliable for real-world use cases.

Acknowledgements
LangChain
HuggingFace
ChromaDB
FastAPI

License
This project is licensed under the MIT License.
