"""
WSGI config for ChatGPT_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# КОД ДЖАНГО ПО-УМОЛЧАНИЮ
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatGPT_site.settings')
application = get_wsgi_application()
