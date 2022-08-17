from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"route": "index"}


@app.post("/create")
def create():

    user = {
        "name": "ismael",
        "age": "620"
    }

    return user
