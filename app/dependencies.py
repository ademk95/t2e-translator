from services.translator_service import TranslatorService

def get_translator_service():
    return _translator_service_instance

_translator_service_instance = TranslatorService()