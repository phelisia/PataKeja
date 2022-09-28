# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': 'kejaproject',
        'USER': 'kejauser',
        'PASSWORD': 'keja',
        'HOST': 'localhost',
        'PORT': 5432,
    }

}