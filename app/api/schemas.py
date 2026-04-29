from pydantic import BaseModel
from typing import List, Dict


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str