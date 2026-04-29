from langchain_google_genai import ChatGoogleGenerativeAI
from app.utils.logger import logger
import os

def generate_answer(query, docs):
    try:
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are an expert AI assistant.

STRICT RULES:
- Use ONLY the provided context
- If answer is not in context, say: "I don't know based on the provided document"
- Be concise and accurate
- Do NOT hallucinate

CONTEXT:
{context}

QUESTION:
{query}

FINAL ANSWER:
"""

        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.3
        )

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
        logger.error(f"Generation failed: {str(e)}")
        return "Error generating answer"