import os
import dj_database_url
from django.conf import settings

def config():
    # Production
    if os.getenv('DATABASE_SERVICE_NAME') == 'postgresql':
        default = dj_database_url.config()

    # Development
    else:
        default = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
        }

    return default
