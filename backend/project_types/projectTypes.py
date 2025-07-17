from pydantic import BaseModel

#temporary for early development
#this will be replaced with a more robust type later
class BasePromt(BaseModel):
    prompt: str
    user: str = "placeholder till auth system is implemented"
    model: str = "gemma3"

