from fake_useragent import FakeUserAgent
from requests import Session

class uuidGeneratorNet:
    def __init__(self):
        self.url = 'https://www.uuidgenerator.net/{}/bulk.json?amount={}'.format
        self.session = Session()
        self.headers = {'user-agent': FakeUserAgent().random}

    def uuid1(self, amount : int):
        req = self.session.get(url = self.url('version1', amount), headers = self.headers)
        return req.json()

    def uuid4(self, amount : int):
        req = self.session.get(url = self.url('version4', amount), headers = self.headers)
        return req.json()