#! /usr/bin/python
import unittest
from BssTestHttp import BssTestHttp
from logger import logger




#Rest server test. Updating user details on a remote server
#using public api https://gorest.co.in/public-api as rest server instead of  http://dummy.restapiexample.com/. sending 303 error using PUT method
    
class TestBssHttp(unittest.TestCase):

    def __init__(self, testname,
                 base_url = 'https://gorest.co.in/public-api',
                 http_address = 'posts/137',
                 ex_response = '200',
                 put_data = { "name": "John Smith" },
                 user_id = '/users/123'):
        
        self.logger = logger(self.__class__.__name__)
        self.logger.info("__init__() called")
        super(TestBssHttp, self).__init__(testname)


        self.logger.info("testname: %s" % testname)
        self.test_bss = None
        self.BASE_URL = base_url
        self. http_address =  http_address
        self.ex_response = ex_response
        self.response = None
       
       
        self.test_url = None
        self.put_data = put_data
        self.user_id = user_id
        self.startUP()

    #setting up the test environment

    def startUP(self):



       
        self.test_url = "%s/%s" % (self.BASE_URL, self.http_address)
        self.test_bss = BssTestHttp(
                                    {
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                    'Accept-Encoding': 'application/json'
                                    }
                                    )
        self.response = self.test_bss.get_request(self.test_url )
        self.logger.info("Get response: %s" % (self.response))

    def tearDown(self):
           del self.test_bss





    #testing get method to make sure the server is up and running. Set failed if response: None, Wrong status code
    def test_for_get_response(self):

         self.assertIsNotNone(self.response, msg = self.logger.info("GET: Response: %s" % self.response))

    def test_for_get_status_code(self):

         self.assertEqual(int(self.ex_response), self.response.status_code, msg= self.logger.info("GET:Status: %s" % self.response.status_code))

    






    #updating record on a server. Set failed if response: None, Wrong status code
    def test_for_put_method(self):


        self.response = None
        self.test_url = "%s/%s" % (self.BASE_URL, self.user_id)

        self.response = self.test_bss.put_request(url = self.test_url, data=self.put_data)
        self.logger.info("PUT response : %s" % (self.response))
        
        self.assertIsNotNone(self.response, msg = self.logger.info("PUT:Response: %s" % self.response))
        self.assertEqual(int(self.ex_response), self.response.status_code, msg=self.logger.info("PUT:Status code: %s" % self.response.status_code))

        



if __name__ == "__main__":
    unittest.main()



