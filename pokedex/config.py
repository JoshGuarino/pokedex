import random
import string

class Config(object):
    SECRET_KEY = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(22))
    DEBUG = True 
    THREADED = True
    RESULTS_PER_PAGE = 60