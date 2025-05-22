from flask import Blueprint, request, jsonify
from app.services.ocr_service import OCRService
import logging

bp = Blueprint('ocr', __name__, url_prefix='/ocr')
ocr_service = OCRService()

@bp.route("", methods=["POST"])
def ocr_image():
    image_file = request.files.get('image')
    if not image_file or image_file.filename == "": return jsonify({"status": False, "message": "No image uploaded"}), 400
    try:
        result = ocr_service.do_ocr(image_file)
        return jsonify({"status": True, "text": result})
    except Exception as e:
        return jsonify({"status": False, "message": str(e)}), 500