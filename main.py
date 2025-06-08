from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello World"


@app.get("/test1")
def index1():
    return "Hello World"