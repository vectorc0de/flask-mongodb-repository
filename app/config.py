import os

class Config:
    MONGO_SERV = os.environ.get('MONGO_SERV') or 'localh0t'
    MONGO_USR = os.environ.get('MONGO_USR') or 'vectorc0de'
    MONGO_PWD = os.environ.get('MONGO_PWD') or 'miakhalifa'

    MONGODB_SETTINGS = {
        'db': 'job_board',
        'host': os.environ.get('MONGODB_URI') or 'mongodb://localhost/job_board'
    }
