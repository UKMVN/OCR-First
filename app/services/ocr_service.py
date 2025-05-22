import numpy as np
import io, easyocr
from PIL import Image
from app.config import Config

class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(
            Config.OCR_LANGUAGES,
            model_storage_directory=Config.OCR_MODEL_DIR,
            quantize=Config.OCR_QUANTIZE
        )

    def do_ocr(self, image):
        pil_image = Image.open(io.BytesIO(image.read()))
        pil_imae = pil_image.convert('RGB')

        w, h = pil_imae.size
        if max(w, h) > Config.MAX_IMAGE_SIZE:
            scale = Config.MAX_IMAGE_SIZE / max(w, h)
            pil_image = pil_image.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        opencv_image = np.array(pil_image)
        results = self.reader.readtext(
            opencv_image,
            batch_size=Config.OCR_BATCH_SIZE,
            paragraph=Config.OCR_PARAGRAPH,
            detail=Config.OCR_DETAIL,
            contrast_ths=Config.OCR_CONTRAST_THS,
            adjust_contrast=Config.OCR_ADJUST_CONTRAST
        )

        return ' '.join(results)