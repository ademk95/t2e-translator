from pydantic import BaseModel

class TranslateResponse(BaseModel):
    translated: str