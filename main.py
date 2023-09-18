from fastapi import FastAPI
app = FastAPI()

@app.get("/bfhl")
def hello():
    return ("Hello world!!!!")

@app.post("/bfhl")
def world(name : str):
    return name
