import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGODB_SETTINGS = {
        'db': 'job_board',
        'host': os.environ.get('MONGODB_URI') or 'mongodb://localhost/job_board'
    }
