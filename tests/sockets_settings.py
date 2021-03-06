from .base_settings import *
from os.path import join, dirname


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': join(dirname(__file__), 'redis.sock'),
        'OPTIONS': { # optional
            'DB': 15,
            'PASSWORD': 'yadayada',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
    },
}

