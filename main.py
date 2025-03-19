from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI(
    docs_url="/api/docs",    # Correct Swagger path
    redoc_url="/api/redoc"   # Correct ReDoc path
)

@app.get("/api/")
def read_api():
    return {"Hello": "Daniel"}

@app.get("/api/test/")
def read_test():
    return {"We": "got this"}

@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("index.html")
