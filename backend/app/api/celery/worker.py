import os
import requests
from time import sleep

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task():
    answ =  requests.post('https://gttb.guane.dev/api/workers?task_complexity=10', {'params': 5}).json()
    return answ