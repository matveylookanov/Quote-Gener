from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from app.models import Quote
        db.create_all()

    from app.routes import main
    app.register_blueprint(main)

    from app.api.endpoints import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
