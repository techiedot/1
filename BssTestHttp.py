#! /usr/bin/python
import requests
from logger import logger
import json
import time



class BssTestHttp(object):

    def __init__(self, header):

        self.logger = logger(self.__class__.__name__)
        self.header = header
        self.logger.debug("Create instance  =  %s" % (self.header))


    def put_request(self, url, headers=None, data=None):

        self.logger.debug("Put requests called with url: %s" % url)
        if headers is None:
            headers = self.header
        
        return_value = requests.put(url=url, headers = headers, data = data)
        self.logger.debug("Put requests status code: %s" % return_value.status_code)
        return return_value



    def get_request(self, url):

        self.logger.debug("Get request called on url: %s", url)
        return_value = requests.get(url)
        self.logger.debug("Get request status code: %s" % return_value.status_code)
        return return_value



    def __del__(self):
        print('Distractor call.')
