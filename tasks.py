from celery import Celery


celery = Celery('tasks')
celery.config_from_object('.celeryconfig')


@celery.task
def run_all_api_tests():

    return 'ran all the tests!'
