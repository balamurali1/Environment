"""
WSGI config for gs17_1_ModelViewSet_and_ReadyOnlyModelViewSet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs17_1_ModelViewSet_and_ReadyOnlyModelViewSet.settings')

application = get_wsgi_application()
