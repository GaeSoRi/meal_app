from flask import Flask, Blueprint

def init_app(app):
    from app.routes.meal import meal_bp

    app.register_blueprint(meal_bp, url_prefix='/meal')
