from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    source: str
    target: str