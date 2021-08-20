from main.settings import BASE_DIR


SECRET_KEY = 'mrmoyp4=@x8k8fc-&s#=4^%*vqqq6ewab&u3xptc12!kwjd-93'


SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name_database',
        'USER': 'user_database',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name_database',
        'USER': 'user_database',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


EMAIL_HOST_USER = 'mail@domain.ru'
EMAIL_HOST_PASSWORD = 'password'