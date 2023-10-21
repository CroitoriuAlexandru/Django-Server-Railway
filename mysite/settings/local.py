from .base import *


STATICFILES_DIRS += [
    os.path.join(BASE_DIR, "theme/static"),
    os.path.join(BASE_DIR, "theme/static_src/node_modules/flowbite/dist"),
    ]

ALLOWED_HOSTS = ["127.0.0.1"]

INTERNAL_IPS = [
    "127.0.0.1",
]