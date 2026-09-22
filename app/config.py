import os

class GeneralConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ADMIN_EMAIL = "johnadeboye50@gmail.com"

class TestingConfig(GeneralConfig):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LiveConfig(GeneralConfig):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False