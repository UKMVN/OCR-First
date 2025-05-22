from flask import Flask

def create_application() -> Flask:
    app = Flask(__name__)

    from app.routes import scene_detect
    app.register_blueprint(scene_detect.bp)

    from app.routes import ocr
    app.register_blueprint(ocr.bp)

    return app