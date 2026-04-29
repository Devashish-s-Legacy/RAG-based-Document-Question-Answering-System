cache = {}
from fastapi import HTTPException
from app.rag.retrieve import get_retriever
from app.rag.generate import generate_answer
from app.utils.logger import logger


class RAGService:

    def __init__(self):
        self.retriever = get_retriever()

    def query(self, question: str):
        try:
            logger.info(f"📥 Query received: {question}")

            docs = self.retriever.invoke(question)
            logger.info(f"📄 Retrieved {len(docs)} documents")

            if question in cache:
                return cache[question]
            if not docs:
                return {
        "question": question,
        "answer": "No relevant documents found.",
        "sources": [],
        "confidence": 0.0
                }

            answer = generate_answer(question, docs)

            logger.info("✅ Answer generated successfully")

            sources = [
    {
        "content": doc.page_content[:200],
        "metadata": doc.metadata
    }
    for doc in docs
            ]
            
            confidence = min(len(docs) / 5, 1.0)

            return {
                "question": question,
                "answer": answer,
                "sources": sources,
                "confidence": 0.7
            }

        except HTTPException as e:
            raise e

        except Exception as e:
            logger.error(f"❌ Internal Error: {str(e)}")

            raise HTTPException(
                status_code=500,
                detail=f"Internal error: {str(e)}"
            )


# singleton instance
rag_service = RAGService()