from .img_online.views import image_bp


def init_app(app):
    app.register_blueprint(image_bp)
