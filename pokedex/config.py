from key_gen import generate_key

class Config(object):
    SECRET_KEY = generate_key()
    DEBUG = True 
    THREADED = True