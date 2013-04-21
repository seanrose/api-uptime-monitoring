from celery import Celery
from APIRequest import APIRequest


celery = Celery('tasks')
celery.config_from_object('.celeryconfig')


@celery.task
def make_box_request():

    box_request = APIRequest(
        http_method='GET',
        url='https://api.box.com/2.0/folders/0/items',
        headers={'Authorization': 'Bearer tOIrDJr2bOoEn9QUFxWSBrc3Z0DSnXX9'}
    )

    for x in xrange(10):
        box_request.make_request()
        box_request.save_request()
        print '{} completed'.format(x)
