#Этот файл обеспечивает корректное подключение к серверу.
#ASGI - более новый стандарт по сравнению с WSGI.
"""
ASGI config for itproger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itproger.settings')

application = get_asgi_application()
