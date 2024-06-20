import requests
from json import dumps
from config.load_config import config
from common.logger import logger

class URLClient():

    def __init__(self):
        self.__session = requests.session()
        self.__url = config.url
    
    def get(self, path, **kwargs):
        res = self.request(path, "GET", **kwargs)
        logger.info(f"status_code ==>> {res.status_code}")
        logger.info(f"response ==>> {res.text}")
        return res

    def post(self, path, data=None, json=None, **kwargs):
        res = self.request(path, "POST", data, json, **kwargs)
        logger.info(f"status_code ==>> {res.status_code}")
        logger.info(f"response ==>> {res.text}")
        return res

    def put(self, path, data=None, **kwargs):
        res = self.request(path, "PUT", data, **kwargs)
        logger.info(f"status_code ==>> {res.status_code}")
        logger.info(f"response ==>> {res.text}")
        return res

    def delete(self, path, **kwargs):
        res = self.request(path, "DELETE", **kwargs)
        logger.info(f"status_code ==>> {res.status_code}")
        logger.info(f"response ==>> {res.text}")
        return res

    def patch(self, path, data=None, **kwargs):
        res = self.request(path, "PATCH", data, **kwargs)
        logger.info(f"status_code ==>> {res.status_code}")
        logger.info(f"response ==>> {res.text}")
        return res

    def request(self, path, method, data=None, json=None, **kwargs):
        url = self.__url + path
        data = dumps(data) if data else None
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.__logs(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.__session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            return self.__session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.__session.delete(url, **kwargs)
        if method == "PATCH":
            return self.__session.patch(url, data, **kwargs)

    def __logs(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info(f"url ==>> {url}")
        logger.info(f"method ==>> {method}")
        if headers:
            logger.info(f"headers ==>> {dumps(headers, indent=4, ensure_ascii=False)}")
        if params:
            logger.info(f"params ==>> {dumps(params, indent=4, ensure_ascii=False)}")
        if data:
            logger.info(f"data ==>> {dumps(data, indent=4, ensure_ascii=False)}")
        if json:
            logger.info(f"json ==>> {dumps(json, indent=4, ensure_ascii=False)}")
        if files:
            logger.info(f"files ==>> {files}")
        if cookies:
            logger.info(f"cookies ==>> {cookies}")
