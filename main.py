from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/api/")
def read_api():
    return {"Hello": "Daniel"}

@app.get("/api/test/")
def read_test():
    return {"We": "got this"}

@app.get("/", response_class=FileResponse)
def root():
    return FileResponse("index.html")
