"""
ASGI config for gs14_Generic_API_Views_Mixins project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs14_Generic_API_Views_Mixins.settings')

application = get_asgi_application()
