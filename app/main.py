import os
import json
import socket
from fastapi import FastAPI

app = FastAPI()


def find_to_env(name: str) -> str:
    result = "No content :("
    if name.upper() in os.environ:
        result = os.environ[name.upper()]
    return result


@app.get("/hostname")
def get_hostname():
    result = socket.gethostname()
    return result


@app.get("/author")
def get_author():
    return find_to_env("author")


@app.get("/id")
def get_id():
    return find_to_env("uid")
