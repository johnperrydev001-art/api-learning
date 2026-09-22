from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()

def create_app():
    from app import config

    app = Flask(__name__,
                instance_relative_config=True,
                template_folder='templates',
                static_folder='static'
                )
    app.config.from_object(config.LiveConfig)
    app.config.from_pyfile('config.py', silent=True)

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app import models

    return app

app = create_app()

from app import routes






