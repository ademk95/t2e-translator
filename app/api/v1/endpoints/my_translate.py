from dto.translate_request_dto import TranslateRequest
from core.config import Settings
from fastapi import APIRouter, Depends
import logging
import dependencies as dependency
import traceback
from fastapi.responses import JSONResponse

settings = Settings()
logger = logging.getLogger(settings.logger_name)
logger.setLevel(settings.log_level)

router = APIRouter()

@router.post("/translate")
async def ask_question(dto: TranslateRequest):    
    try:
        service = dependency.get_translator_service()
        result = service.translate(dto.text, dto.source, dto.target)
        return {"success": True, "message": result}
    except Exception as ex:
        stack_trace = traceback.format_exc()
        logger.error(f"❌ [My Translate] Error: {ex} Trace: {stack_trace}")        
        return JSONResponse(
            status_code=500,
            content={ "success": False, "message": "E:IntervalServer"}
        )