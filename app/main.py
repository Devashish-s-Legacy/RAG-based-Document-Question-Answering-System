from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FIRST create app
app = FastAPI()

# THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# THEN import routes
from app.api.routes import router as query_router
from app.api.upload_routes import router as upload_router
from app.api.eval_routes import router as eval_router

# THEN include routers
app.include_router(query_router)
app.include_router(upload_router)
app.include_router(eval_router)


