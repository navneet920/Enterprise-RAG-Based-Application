from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME")

    HUGGINGFACE_API_KEY = os.getenv(
        "HUGGINGFACE_API_KEY"
    )

    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    MONGO_URI = os.getenv("MONGO_URI")

    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")


settings = Settings()