import APIRequest
# figure out some shit to do with celery


class APITest(object):
    """THe container for API tests"""

    def __init__(self, api_test_id):

        self.api_test_id = api_test_id

    def log_request(self):
        """
        Makes the API request and logs its response time
        """

        api_request = APIRequest.get(api_test_id=self.api_test_id)
        api_request.make_request()
        # save self.api_request.elapsed somehow
