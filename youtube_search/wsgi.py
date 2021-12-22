"""
WSGI config for youtube_search project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from threading import Thread
from django.core.wsgi import get_wsgi_application
from api.utils import start_youtube_search

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_search.settings')

application = get_wsgi_application()
Thread(target=start_youtube_search, args=("cricket","youtube","v3")).start()