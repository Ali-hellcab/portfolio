"""
WSGI config for portfolio_site project.

It exposes the WSGI callable as a module-level variable named ``application``.
Used by Gunicorn and other WSGI servers in production.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

application = get_wsgi_application()
