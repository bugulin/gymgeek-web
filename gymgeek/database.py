import os
from django.conf import settings

def config():
    # Production
    if os.getenv('DATABASE_SERVICE_NAME') == 'postgresql':
        default = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('POSTGRESQL_SERVICE_HOST'),
            'PORT': os.getenv('POSTGRESQL_SERVICE_PORT'),
        }

    # Development
    else:
        default = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
        }

    return default
