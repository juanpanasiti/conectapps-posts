import requests


class PostsExternalInterface:
    def __init__(self, base_url, headers={}):
        self.__client = None
        self.__base_url = base_url
        self.__headers = headers

    @property
    def client(self):
        if self.__client is None:
            self.__client = requests.Session()
        return self.__client

    def __make_url(self, path):
        return self.__base_url + path

    def __make_headers(self, headers):
        return {**self.__headers, **headers}

    def get(self, path='', new_headers={}):
        url = self.__make_url(path)
        headers = self.__make_headers(new_headers)

        response = self.client.get(url, headers=headers)

        return response.json()
