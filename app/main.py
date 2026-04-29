from fastapi import FastAPI
from app.api.routes import router as query_router
from app.api.upload_routes import router as upload_router
from app.api.eval_routes import router as eval_router

app = FastAPI()

# ✅ Register routes AFTER app is created
app.include_router(query_router)
app.include_router(upload_router)
app.include_router(eval_router)


@app.get("/")
def root():
    return {"message": "RAG API is running 🚀"}