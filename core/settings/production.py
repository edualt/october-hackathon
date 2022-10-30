from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = [
    '*',
    ]

CORS_ALLOWED_ORIGINS = [
    'http://*',
    'https://october-hackathon-edualt.up.railway.app'
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'URL': env.str('DB_URL'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env.str('CLOUD_NAME'),
    'API_KEY': env.str('API_KEY'),
    'API_SECRET': env.str('API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Media files
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

MEDIA_URL = 'media/'
