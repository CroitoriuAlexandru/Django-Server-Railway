from .base import *


ALLOWED_HOSTS = ["django-server-production-00ab.up.railway.app"]

# FORM SUBMISSION
# Comment out the following line and place your railway URL, and your production URL in the array.
CSRF_TRUSTED_ORIGINS = ["https://django-server-production-00ab.up.railway.app"]

SESSION_COOKIE_SECURE = True # handle security.W012
CSRF_COOKIE_SECURE = True # handle security.W016
SECURE_SSL_REDIRECT = True # handle security.W008
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # necesary for SECURE_SSL_REDIRECT as it runs with a proxy


SECURE_HSTS_SECONDS = 31536000 # handle security.W004 
SECURE_HSTS_PRELOAD = True # handle security.W019
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # handle security.W005