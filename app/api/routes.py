from fastapi import APIRouter
from app.services.rag_service import rag_service

router = APIRouter()


from app.api.schemas import QueryRequest, QueryResponse

@router.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    return rag_service.query(request.query)

@router.get("/health")
def health():
    return {"status": "ok"}