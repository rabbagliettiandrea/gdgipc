from celery import Celery
from . import tasks

celery_app = Celery('ipc_python', broker='pyamqp://guest:guest@localhost//')
celery_app.conf.result_backend = 'rpc://'
