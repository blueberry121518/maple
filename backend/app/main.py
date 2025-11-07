from fastapi import FastAPI


app = FastAPI(title="Maple API", version="0.1.0")


@app.get("/")
async def root():
  return {"message": "Hello from Maple FastAPI!"}

