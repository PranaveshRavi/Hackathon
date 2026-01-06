# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(
    title="Sample FastAPI App",
    description="A minimal FastAPI example running on port 300",
    version="1.0.0"
)

# Allow all origins (you can restrict this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI running on port 300!"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=300, reload=True)
