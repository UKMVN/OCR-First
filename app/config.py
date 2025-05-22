import os, torch

class Config:
    OCR_LANGUAGES = ['en']
    OCR_MODEL_DIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "models")
    OCR_QUANTIZE = True
    MAX_IMAGE_SIZE = 1600
    OCR_BATCH_SIZE = 4
    OCR_PARAGRAPH = True
    OCR_DETAIL = 0
    OCR_CONTRAST_THS = 0.1
    OCR_ADJUST_CONTRAST = 0.5

    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8080))
    THREADED = True