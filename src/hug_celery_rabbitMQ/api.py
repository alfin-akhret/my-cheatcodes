"""first api, local access only"""
import hug
import celery
from queues.tasks.happy_birthday import happy_birthday

@hug.get(examples='name=Alfin&age=30')
@hug.local()
def hbd(name: hug.types.text,
    age: hug.types.number, hug_timer=3):
    """Say Happy Birthday to user"""
    happy_birthday.delay(name, age)
    return {'message': 'Done',
        'took': float(hug_timer)}