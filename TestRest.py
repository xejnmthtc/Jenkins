import pytest
import requests


class MyRequest:

    def __init__(self, url,method):
        if method == 'get':
            self.response = requests.get(url)
        elif method == 'post':
            self.response = requests.post(url)
        elif method == 'put':
            self.response = requests.put(url)
        elif method == 'delete':
            self.response=requests.delete(url)

    def get_response(self):
        return self.response

    def get_status(self):
        return self.response.status_code

    def get_page(self):
        return self.response.text

    def allowed(self):
        return self.response.ok

    def get_url(self):
        return  self.response.url

    def get_headers(self,):
        return self.response.headers

    def send_auth_request(self,username,password):
        url =self.response.url
        url = url + '/basic-auth/' +username + '/' +password
        ##https://httpbin.org/basic-auth/user/name
        self.response = requests.get(url , auth=(username,password))




@pytest.fixture()
def data():
    data = MyRequest('https://google.com','get')
    return data


def test_get(data):
    expected = 200
    actual =data.get_status()
    assert expected == actual
