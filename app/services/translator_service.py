import logging
import torch
from core.config import Settings
from transformers import M2M100Tokenizer, M2M100ForConditionalGeneration

settings = Settings()
logger = logging.getLogger(settings.logger_name)
logger.setLevel(settings.log_level)

model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name, token=settings.hface_token)
model = M2M100ForConditionalGeneration.from_pretrained(model_name, token=settings.hface_token)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

class TranslatorService:
    def translate(self, text, source, target):
        tokenizer.src_lang = source
        encoded = tokenizer(text, return_tensors="pt").to(device)
        out = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id(target), num_beams=1)
        return tokenizer.decode(out[0], skip_special_tokens=True)

# import logging
# from core.config import Settings
# from deep_translator import GoogleTranslator

# class TranslatorService:
#     def __init__(self):
#             self.settings = Settings()
#             self.logger = logging.getLogger(self.settings.logger_name)
#             self.logger.setLevel(self.settings.log_level)            

#     def translate(self, text, source, target):
#         return GoogleTranslator(source=source, target=target).translate(text)