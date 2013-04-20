from celery import Celery

celery = Celery('tasks')
celery.config_from_object('.celeryconfig')


@celery.task
def do_something():
    print 'hello'
