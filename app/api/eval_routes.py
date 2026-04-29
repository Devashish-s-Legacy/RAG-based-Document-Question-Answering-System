from fastapi import APIRouter
from app.services.rag_service import RAGService

router = APIRouter()
rag = RAGService()

@router.get("/eval")
def evaluate():
    test_questions = [
        "What is this document about?",
        "Summarize the main topic"
    ]

    results = []

    for q in test_questions:
        result = rag.query(q)
        results.append({
            "question": q,
            "answer": result["answer"],
            "confidence": result["confidence"]
        })

    return {"results": results}