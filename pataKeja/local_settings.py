# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME': 'kejaproject',
        'USER': 'kejauser',
        'PASSWORD': 'keja',
        'HOST': 'localhost',
        'PORT': 5432,
    }

}