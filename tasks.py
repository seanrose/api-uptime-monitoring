from celery import Celery
import api_test


celery = Celery('tasks')
celery.config_from_object('.celeryconfig')


@celery.task
def run_all_api_tests():

    all_tests = api_test.fetch_api_tests()

    for test in all_tests:
        classed = api_test.APITest(*test)
        classed.run_test()
