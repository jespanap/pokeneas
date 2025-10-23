from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import pokenea_bp
    app.register_blueprint(pokenea_bp)

    return app
