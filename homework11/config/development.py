import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
FLASK_RANDOM_SEED = 1

DEBUG = True
SECRET_KEY = 'This key must be secret!'
WTF_CSRF_ENABLED = False
