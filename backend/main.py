from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.ollama_endpoints import router as ollama_router


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # change this
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],

)

app.include_router(ollama_router, prefix="/api/v1", tags=["prompts"])

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}