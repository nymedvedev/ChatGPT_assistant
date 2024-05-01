"""
ASGI config for ChatGPT_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# это новый код, который я прописал с целью асинхронного выполнения программы:
import os
import django
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatGPT_site.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
})


# это исходный код Django для файла ASGI (был тут по-умолчанию)
"""
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatGPT_site.settings')
application = get_asgi_application()
"""
