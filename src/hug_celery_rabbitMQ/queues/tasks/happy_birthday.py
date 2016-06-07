#import celery_daemon
from queues.celery_daemon import celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery.task
def happy_birthday(name, age):
    logger.info('Saying happy birthday to {}'.format(name))
    return 'Happy {0} Birthday {1}'.format(age, name)