from __future__ import absolute_import
from celery import Celery

# instantiate Celery object
celery = Celery(include=['queues.tasks.happy_birthday'])

# import celery config file
celery.config_from_object('config.celeryconfig')

if __name__ == '__main__':
    celery.start()