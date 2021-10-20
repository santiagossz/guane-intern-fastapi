# import os
# import time

# from celery import Celery


# celery = Celery("worker",
#         backend="redis://:password123@redis:6379/0",
#         broker="amqp://user:bitnami@rabbitmq:5672//")

# celery.conf.task_routes={"backend.app.api.worker."}

# celery.conf.task_routes = {
#         "backend.app.api.worker.test_celery": "test-queue"}

# celery.conf.update(task_track_started=True)