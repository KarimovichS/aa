
from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     "default": {
#         "ENGINE": config("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": config("SQL_DATABASE", BASE_DIR / "db.sitqle3"),
#         "USER": config("SQL_USER", "user"),
#         "PASSWORD": config("SQL_PASSWORD", "password"),
#         "HOST": config("SQL_HOST", "localhost"),
#         "PORT": config("SQL_PORT", "5432"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE"),
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
    }
}