from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from app.auth import bp as auth_bp
    from app.main import bp as main_bp
    from app.posts import bp as posts_bp
    from app.comments import bp as comments_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(comments_bp)

    from app import models   # ✅ IMPORTANT

    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

    return app
