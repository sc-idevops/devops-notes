"""
WSGI config for django_auth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auth.settings')
if settings.DEBUG:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = StaticFilesHandler(get_wsgi_application())
    #application = get_wsgi_application()