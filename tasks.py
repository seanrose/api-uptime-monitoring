from celery import Celery
from APIRequest import APIRequest


celery = Celery('tasks')
celery.config_from_object('.celeryconfig')


@celery.task
def make_box_request():

    box_request = APIRequest(
        http_method='GET',
        url='https://api.box.com/2.0/search?query=files',
        headers={'Authorization': 'Bearer OAfKMauM7ruXcY8vFLNt1A44r4uXGsb3'}
    )

    for x in xrange(3):
        box_request.make_request()
        box_request.save_request()
        print '{} completed'.format(x)
