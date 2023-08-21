from fastapi import FastAPI

app = FastAPI()


@app.get("/hostname")
def get_hostname():
    return {"hostname": "hostname"}


@app.get("/author")
def get_author():
    return {"author": "author"}


@app.get("/id")
def get_id():
    return {"id": "id"}
