from fastapi import FastAPI

from api.v1.ollama_endpoints import router as ollama_router

app = FastAPI()
app.include_router(ollama_router, prefix="/api/v1", tags=["prompts"])

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"} 