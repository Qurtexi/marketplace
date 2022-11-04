from os import environ
import databases

DB_USER = environ.get("DB_USER", "marketplace_project")
DB_PASSWORD = environ.get("DB_PASSWORD", "sawA22saw221")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "marketplace_project"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
