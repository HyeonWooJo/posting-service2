from .base import *

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.environ.get("DB_NAME"),
#         "PASSWORD": os.environ.get("DB_ROOT_PASSWORD"),
#         "HOST": os.environ.get("DB_HOST"),
#         "PORT": os.environ.get("DB_PORT"),
#         "OPTIONS": os.environ.get("OPTIONS")
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "things",
        "USER": "user",
        "PASSWORD": "user",
        "HOST": "mysql",
        "PORT": "3306",
        "OPTIONS": {'charset': 'utf8mb4'}
    }
}