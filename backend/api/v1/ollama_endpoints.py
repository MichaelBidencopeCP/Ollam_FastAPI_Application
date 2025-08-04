from fastapi import APIRouter, HTTPException
from project_types.projectTypes import BasePromt
import ollama
router = APIRouter()


@router.post("/ollama/ask", response_model=dict)
async def ask_ollama(prompt: BasePromt):
    """
    Endpoint to ask Ollama a question.
    """
    try:
        response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt.prompt}])
        if not response:
            raise HTTPException(status_code=500, detail="No response from Ollama")
        #remove <think>...</think> tags if they exist and anything inside them
        if "</think>" in response['message']['content']:
            response = response['message']['content'][response['message']['content'].index("</think>") + 8:]
        else:
            response = response['message']['content']
        response = {"response": response}
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))