from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/")
def read_root():
    return {"Hello": "Daniel"}

@app.get("/api/test/")
def read_test():
    return {"We": "got this"}