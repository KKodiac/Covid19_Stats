from fastapi import FastAPI

app = FastAPI()

@app.post("/World")

@app.post("/Korea/")
async def post():
    print("홍섬민 바보")


@app.get("/")
async def root():
    return {"message": "Hello World"}