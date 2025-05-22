from flask import Blueprint, request, jsonify
from app.services.scene_clf import SceneDetector

bp = Blueprint('detect_scene', __name__, url_prefix='/detect_scene')
scene_detect = SceneDetector()

@bp.route("", methods=['POST'])
def detect_scene():
    images = request.files.get('image')
    if not images or images.filename == '': {"status": False, "message": "Image not found"}
    try:
        result = scene_detect.do_predict(images)
        return jsonify(result)
    except Exception as e:
        return {"status": False, "message": str(e)}