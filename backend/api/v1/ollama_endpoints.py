from fastapi import APIRouter, HTTPException
from project_types.projectTypes import BasePromt
router = APIRouter()


@router.post("/prompt")
async def process_prompt(prompt:BasePromt):
    if not prompt.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    # Here you would typically process the prompt with the specified model
    # For now, we will just return the prompt as a response
    return {
        "message": "Prompt processed successfully",
        "prompt": prompt.prompt,
        "user": prompt.user,
        "model": prompt.model
    }


