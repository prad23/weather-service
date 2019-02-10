import requests, logging

log = logging.getLogger(__name__)


class HttpClient(object):

    def __init__(self, url=None, params=None, response=None):
        self.url = url
        self.params = params
        self.response = response

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params

    def __getstatus(self, response):
        self.response = response
        return self.response.status_code

    def __getbody(self):
        body = self.response.json()
        return body

    def __getresponse(self):
        if self.__getstatus(self.response) == 200:
            return self.__getbody()
        else:
            raise Exception("Response status code returned: %s" % self.response)

    def get_request(self):
        if self.params is not None:
            self.response = requests.get(self.url, self.params)
            log.info("+++ Base URL with Parameters: Method--> GET :: %s +++" % (self.response.url))
        else:
            self.response = requests.get(self.url)
            log.info ("+++ Base URL: Method--> GET :: %s +++" % (self.response.url))
        return self.__getresponse()
