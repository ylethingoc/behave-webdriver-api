import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIBase:
    requests = requests

    def __init__(self, url):
        if url[-1:] == '/':
            self.url = url
        else:
            self.url = url + '/'

    def get(self, path, headers, auth=None):
        return self.requests.get(url=self.combine(path), headers=headers, verify=False, auth=auth)

    def put(self, path, body, headers):
        return self.requests.put(url=self.combine(path), json=body, headers=headers, verify=False)

    def post(self, path, body, headers):
        return self.requests.post(url=self.combine(path), json=body, headers=headers, verify=False)

    def combine(self, path):
        if path[:1] != '/':
            return '{}{}'.format(self.url, path)
        else:
            return '{}{}'.format(self.url, path[1:])