#! /usr/bin/python
import requests
import HTTP_code as StatusCodes
from logger import logger
from threading import Thread
import json
import time



class YellowDogRestApi(object):

    def __init__(self, header, timeout=0.2):

        self.logger = logger(self.__class__.__name__)


        self.header = header
        self.timeout = timeout
        self.limit_timeout = timeout  # 200.ms
        self.logger.debug("Create instance of YellowDogRestApi  called on header =  %s, timeout = %s" % (
        self.header, self.limit_timeout))
        self.verificationErrors = []

    def put_request(self, url, headers=None, data=None, timeout=None, files=None):

        self.logger.debug("put_request() called on url: %s" % url)

        if headers is None:
            headers = self.header
        if timeout is None:
            timeout = self.timeout

        args = {"headers": headers, "timeout": timeout, "files": files}

        thread = TwV(target=requests.put, args=(url, params), kwargs=args)
        thread.start()
        return_value = thread.join(self.limit_timeout)

        if return_value is not None:
            http_response_time = return_value.elapsed.total_seconds()
            print
            "Time", http_response_time
            if http_response_time > timeout:
                self.logger.debug(
                    "HTTP POST method delay  by more that  %s msec for http address based on the set limit by user: %s" % (
                        (timeout - http_response_time), url))
                timeout_is = True
                delay_by = http_response_time - timeout

            else:
                timeout_is = False
                delay_by = None
        else:
            timeout_is = None
            delay_by = None

        return return_value, timeout_is, delay_by

        if return_value is not None:
            http_response_time = return_value.elapsed.total_seconds()
            print
            "Time", http_response_time
            if http_response_time > timeout:
                self.logger.debug(
                    "HTTP POST method delay  by more that  %s msec for http address based on the set limit by user: %s" % (
                        (timeout - http_response_time), url))
                timeout_is = True
                delay_by = http_response_time - timeout

            else:
                timeout_is = False
                delay_by = None
        else:
            timeout_is = None
            delay_by = None

        return return_value, timeout_is, delay_by

    def get_request(self, url, header=None, data=None, timeout=None, id_number=None):


        self.logger.debug("get_request called on url: %s")
        if timeout is None:
            timeout = self.limit_timeout
        if header is None:
            headers = self.header


        return_value = requests.get(url, headers)


        if return_value is not None:
            http_response_time = return_value.elapsed.total_seconds()

            if http_response_time > timeout:
                self.logger.debug(
                    "HTTP GET method delay  by more that  %s msec for http adress based on the limit set by user: %s" % (
                        (timeout - http_response_time), url))
                timeout_is = True
                delay_by = http_response_time - timeout
                print

            else:
                timeout_is = False
                delay_by = None
        else:
            timeout_is = None
            delay_by = None

        return return_value, timeout_is, delay_by

    def post_request(self, url, data=None, timeout=None, headers=None, files=None):

        if headers is None:
            headers = self.header
        if timeout is None:
            timeout = self.timeout
        self.logger.debug("POST REQUEST: %s" % (files))
        self.logger.debug("Post header =  %s, files = %s, data = %s" % (headers, timeout, data))
        args = {"headers": headers,  "timeout": timeout}
        if data is not None:
            data = json.dumps(files)

        thread = TwV(target=requests.post,
                     args=(url, data),
                     kwargs=args)

        thread.start()

        return_value = thread.join(self.limit_timeout)

        if return_value is not None:
            http_response_time = return_value.elapsed.total_seconds()

            if http_response_time > timeout:
                self.logger.debug(
                    "HTTP POST method delay  by more that  %s msec for http adress based on the set limit by user: %s" % (
                    (timeout - http_response_time), url))
                timeout_is = True
                delay_by = http_response_time - timeout

            else:
                timeout_is = False
                delay_by = None
        else:
            timeout_is = None
            delay_by = None

        return return_value, timeout_is, delay_by

    def delete_request(self, url, header=None, timeout=None):


        if timeout is None:
            timeout = self.timeout

        args = {"headers": self.header, "timeout": self.timeout}
        thread = TwV(target=requests.delete, args=(url,), kwargs=args)
        thread.start()

        return_value = thread.join(self.limit_timeout)

        if return_value is not None:
            http_response_time = return_value.elapsed.total_seconds()
            print
            "Time", http_response_time
            if http_response_time > timeout:
                self.logger.debug(
                    "HTTP POST method delay  by more that  %s msec for http adress based on the set limit by user: %s" % (
                        (timeout - http_response_time), url))
                timeout_is = True
                delay_by = http_response_time - timeout

            else:
                timeout_is = False
                delay_by = None
        else:
            timeout_is = None
            delay_by = None

        return return_value, timeout_is, delay_by




class TwV(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, verbose=None):

        Thread.__init__(self, group, target, name, args, kwargs, verbose)
        self._return = None

    def run(self):

        if self._Thread__target is not None:

            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)

        else:
            self.logger.error("Object no runnable")

    def join(self, timeout=None):

        Thread.join(self, timeout)
        return self._return
