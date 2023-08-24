import os
import json
import socket
from fastapi import FastAPI

app = FastAPI()


RESULT_DICT = {
    "HOSTNAME": socket.gethostname(),
    "AUTHOR": "!!!ANONYMOUS!!!",
    "UID": "!!!UID!!!"
               }


for key in os.environ:
    RESULT_DICT[key] = os.environ[key]


@app.get("/")
def get_all():
    return json.dumps(RESULT_DICT, indent=4)


@app.get("/hostname")
def get_hostname():
    return RESULT_DICT["HOSTNAME"]


@app.get("/author")
def get_author():
    return RESULT_DICT["AUTHOR"]


@app.get("/id")
def get_id():
    return RESULT_DICT["UID"]
