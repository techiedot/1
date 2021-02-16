#! /usr/bin/python

from unittest import TestCase
from YellowDogRestApi import YellowDogRestApi
from logger import logger
import json
import requests
import platform
import HTTP_CODE as HttpCodes
import datetime
debug = True


class TestYellowDog(TestCase):
    
    
    def __init__(self, testname, acc_type="nonesecure", timeout = 0.2, files_out="json_out.txt", files_in = "json_in.txt"):
        
        self.logger = logger(self.__class__.__name__)
        self.logger.info("__init__() called")
        self.fmt = '%Y-%m-%d-%H-%M-%S:'
        super(TestYellowDog, self).__init__(testname)


        self.logger.info("testname: %s" % testname)
        
        
        self.timeout = timeout

        self.BASE_URL = None
        self.rest_yellowdog = None
        self.acc_type = acc_type
        self.verificationErrors = []
        self.files_out = files_out
        self.files_in = files_in

    def startUP(self):
        """
        Lets create instance of the YellowDogRestApi.  Secure version is  for future use. Now we only testing none secure version of the application.
        """
        ACCOUNT = {
                   'nonesecure': 'http://localhost:8080/api',
                   'secure': 'https://localhost/api'
                  }
        self.BASE_URL = ACCOUNT[self.acc_type.lower()]
        self.rest_yellowdog = YellowDogRestApi(
                                                 {
                                                  'Content-Type': 'application/json',
                                                  'Accept': 'application/json; charset=UTF-8'
                                                 }
                                               )


       
    
    def test_create_account(self, ex_response = None, data = "None", header=None, http_address=None,files=None, timeout=None):
        self.logger.debug("create new position")
        if files is None:
            files  = self.files_out
        url = "%s/%s" % (self.BASE_URL, http_address)

        with open(files) as json_file:
                 files = json.load(json_file)
        self.logger.info("JSON DATA: %s" % files)

        if http_address is None:
             self.logger.error("HTTP address to access api interface")

        
        
       
        response, timeout, delay_by = self.rest_yellowdog.post_request(url, data, timeout, header, files)


       
        
       

        if response is None:
             failed =  'ERROR Create account:' + datetime.datetime.now().strftime(self.fmt) + ' '  + 'ERROR Fetch All ' + '' + 'TYPE: Status code is None from url ' + url
             self.verificationErrors.append(failed)
        elif response.HTTP_CODE != ex_response:

	     print("Status code returned: %s meaning (%s); expected: %s (%s)" % (response, HttpCodes.HTTP_CODEs[response.HTTP_CODE],  ex_response, HttpCodes.HTTP_CODEs[ex_response]))
	     m = HttpCodes.HTTP_CODEs[response.HTTP_CODE]
	     failed = 'ERROR Create account:' + 'TIME:' + datetime.datetime.now().strftime(self.fmt) + 'TYPE: Wrong status code from' + ' ' +  'url address' + ' ' + url + ' ' +'Expected value:' +    str(ex_response) +' '+ 'Actuale value:' + ' ' + ' ' + str(response.HTTP_CODE)
	     self.verificationErrors.append(failed)

	elif timeout is True:
             failed = 'ERROR Create account:' + 'TIME:' + datetime.datetime.now().strftime(self.fmt) + ' '  + 'TYPE: Timeout exceed' + ' ' + str(delay_by) + ' ' +  'from url ' + url
             self.verificationErrors.append(failed)
             self.logger.info("RESPONSE CODE OPEN POSITION: %s" % response.HTTP_CODE) 
        else:
             test_pass = datetime.datetime.now().strftime(self.fmt) + ' ' +'Fetch All tets passed ' ' ' +  'TYPE: Timeout, Correct status code, Server up and running' + ' '  +  'from url ' + ' '  + url
             self.logger.info("Create account test pass")
             self.verificationErrors.append(test_pass)





    
    def test_fetch_all_data(self, ex_response = None, header=None, http_address=None, timeout=None, files=None):

        if files is None:
            files = self.files_out
        url = "%s/%s" % (self.BASE_URL, http_address)
        response, timeout, delay_by = self.rest_yellowdog.get_request(url,header,timeout)
        self.logger.info("RESPONSE: %s %s %s" % ( response, timeout, delay_by))



        if response is None:
            failed = 'ERROR Fetch All:' + datetime.datetime.now().strftime(
                self.fmt) + ' ' + 'ERROR Fetch All ' + '' + 'TYPE: Status code is None from url ' + url
            self.verificationErrors.append(failed)
        elif response.HTTP_CODE != ex_response:

            print("Status code returned: %s meaning (%s); expected: %s (%s)" % (
            response, HttpCodes.HTTP_CODEs[response.HTTP_CODE], ex_response,
            HttpCodes.HTTP_CODEs[ex_response]))
            m = HttpCodes.HTTP_CODEs[response.HTTP_CODE]
            failed = 'ERROR Fetch All:' + 'TIME:' + datetime.datetime.now().strftime(
                self.fmt) + 'TYPE: Wrong status code from' + ' ' + 'url address' + ' ' + url + ' ' + 'Expected value:' + str(
                ex_response) + ' ' + 'Actuale value:' + ' ' + ' ' + str(response.HTTP_CODE)
            self.verificationErrors.append(failed)

        elif timeout is True:
            failed = 'ERROR Fetch All:' + 'TIME:' + datetime.datetime.now().strftime(
                self.fmt) + ' ' + 'TYPE: Timeout exceed' + ' ' + str(delay_by) + ' ' + 'from url ' + url
            self.verificationErrors.append(failed)
            self.logger.info("RESPONSE CODE OPEN POSITION: %s" % response.HTTP_CODE)
        else:
            test_pass = datetime.datetime.now().strftime(
                self.fmt) + ' ' + 'Fetch All tets passed ' ' ' + 'TYPE: Timeout limit pass, Correct status code returned, Server up and running' + ' ' + 'from url ' + ' ' + url
            self.logger.info("Fetch all data test pass")
            self.verificationErrors.append(test_pass)







        self.logger.info("Fetching data: %s" % response)

        #sending json the data to file to use as a input values to fetch and update records by id. Only suitable for small scale testing. Use as demonstration purpose only
        if response is not None:
            data = response.json()

            with open(self.files_in, "w") as json_file:
                json.dump(data, json_file)





    def test_fetch_by_id_all(self, ex_response = None, data = "None", header=None, http_address=None,files = None, timeout=None):

        id_list = []

        if files is None:
            files  = self.files_in
        if timeout is None:
            timeout = self.timeout

        url = "%s/%s" % (self.BASE_URL, http_address)
        self.logger.info("JSON DATA: %s" % files)
        correct_format = True
        try:
            with open(files) as json_file:
                   data = json.load(json_file)
        except ValueError as e:
            correct_format = False
            pass

        if correct_format:

            for item in range(len(data)):
                for key, value in data[item].items():
                    if key == 'id':
                       id_list.append(value)


        else:
             print("Wrong json format.")

        if id_list:
            for item in range(len(id_list)):
                url_id = url + '/' + str(id_list[item])

                response, timeout_out, delay_by = self.rest_yellowdog.get_request(url_id, header, timeout)
                self.logger.info("RESPONSE: %s %s %s" % (response, timeout, delay_by))

                if response is None:
                    failed = 'ERROR Fetch All:' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'ERROR Fetch All ' + '' + 'TYPE: Status code is None from url ' + url_id
                    self.verificationErrors.append(failed)
                elif response.HTTP_CODE != ex_response:

                    print("Status code returned: %s meaning (%s); expected: %s (%s)" % (
                        response, HttpCodes.HTTP_CODEs[response.HTTP_CODE], ex_response,
                        HttpCodes.HTTP_CODEs[ex_response]))
                    m = HttpCodes.HTTP_CODEs[response.HTTP_CODE]
                    failed = 'ERROR Fetch All:' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + 'TYPE: Wrong status code from' + ' ' + 'url address' + ' ' + url_id + ' ' + 'Expected value:' + str(
                        ex_response) + ' ' + 'Actuale value:' + ' ' + ' ' + str(response.HTTP_CODE)
                    self.verificationErrors.append(failed)

                elif timeout_out is True:
                    failed = 'ERROR Fetch All:' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'TYPE: Timeout exceed' + ' ' + str(delay_by) + ' ' + 'from url ' + url_id
                    self.verificationErrors.append(failed)
                    self.logger.info("RESPONSE CODE OPEN POSITION: %s" % response.HTTP_CODE)
                else:
                    test_pass = datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'Fetch All by ID passed ' ' ' + 'TYPE: Timeout limit pass, Correct status code returned, Server up and running' + ' ' + 'from url ' + ' ' + url_id
                    self.logger.info("Fetch all data test pass")
                    self.verificationErrors.append(test_pass)
                url_id = ' '
        else:
            self.logger.info("ID list empty" )
            failed = 'ERROR GET data by ID is not completed. ID list is empty:'
            self.verificationErrors.append(failed)




    def test_fetch_by_id(self, ex_response=None, data="None", header=None, http_address=None, files=None, timeout=None, id_number = None):



        if timeout is None:
            timeout = self.timeout
        if id_number is None:
            id_number = '666'
        url = "%s/%s" % (self.BASE_URL, http_address)
        url_id = url + '/' + str(id_number)

        response, timeout_out, delay_by = self.rest_yellowdog.get_request(url_id, header, timeout, id_number = id_number)

        self.logger.info("RESPONSE: %s %s %s" % (response, timeout, delay_by))

        if response is None:
                    failed = 'ERROR Fetch :' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'ERROR Fetch  ' + '' + 'TYPE: Status code is None from url ' + url_id
                    self.verificationErrors.append(failed)
        elif response.HTTP_CODE != ex_response:

                    print("Status code returned: %s meaning (%s); expected: %s (%s)" % (
                        response, HttpCodes.HTTP_CODEs[response.HTTP_CODE], ex_response,
                        HttpCodes.HTTP_CODEs[ex_response]))
                    m = HttpCodes.HTTP_CODEs[response.HTTP_CODE]
                    failed = 'ERROR Fetch :' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + 'TYPE: Wrong status code from' + ' ' + 'url address' + ' ' + url_id + ' ' + 'Expected value:' + str(
                        ex_response) + ' ' + 'Actuale value:' + ' ' + ' ' + str(response.HTTP_CODE)
                    self.verificationErrors.append(failed)

        elif timeout_out is True:
                    failed = 'ERROR Fetch :' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'TYPE: Timeout exceed' + ' ' + str(delay_by) + ' ' + 'from url ' + url_id
                    self.verificationErrors.append(failed)
                    self.logger.info("RESPONSE CODE OPEN POSITION: %s" % response.HTTP_CODE)
        else:
                    test_pass = datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'Fetch  tets passed ' ' ' + 'TYPE: Timeout limit pass, Correct status code returned, Server up and running' + ' ' + 'from url ' + ' ' + url_id
                    self.logger.info("Fetch all data test pass")
                    self.verificationErrors.append(test_pass)






    def test_delete(self, ex_response=None, data="None", header=None, http_address=None, files=None, timeout=None, id_number=None):




        if files is None:
            files  = self.files_in
        if timeout is None:
            timeout = self.timeout
        with open(files) as json_file:
                 files = json.load(json_file)
        self.logger.info("JSON DATA: %s" % files)
        url = "%s/%s" % (self.BASE_URL, http_address)



        url_id = url + '/' + str(id_number)
        response, timeout_out, delay_by = self.rest_yellowdog.delete_request(url_id, header, timeout)
        self.logger.info("RESPONSE: %s %s %s" % (response, timeout_out, delay_by))

        if response is None:
                    failed = 'ERROR Delete :' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'ERROR Fetch  ' + '' + 'TYPE: Status code is None from url ' + url_id
                    self.verificationErrors.append(failed)
        elif response.HTTP_CODE != ex_response:

                    print("Status code returned: %s meaning (%s); expected: %s (%s)" % (
                        response, HttpCodes.HTTP_CODEs[response.HTTP_CODE], ex_response,
                        HttpCodes.HTTP_CODEs[ex_response]))
                    m = HttpCodes.HTTP_CODEs[response.HTTP_CODE]
                    failed = 'ERROR Delete :' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + 'TYPE: Wrong status code from' + ' ' + 'url address' + ' ' + url_id + ' ' + 'Expected value:' + str(
                        ex_response) + ' ' + 'Actuale value:' + ' ' + ' ' + str(response.HTTP_CODE)
                    self.verificationErrors.append(failed)

        elif timeout_out is True:
                    failed = 'ERROR Delete :' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'TYPE: Timeout exceed' + ' ' + str(delay_by) + ' ' + 'from url ' + url_id
                    self.verificationErrors.append(failed)
                    self.logger.info("RESPONSE CODE OPEN POSITION: %s" % response.HTTP_CODE)
        else:
                    test_pass = datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'Delete  test passed ' ' ' + 'TYPE: Timeout limit pass, Function, Correct status code returned, Server up and running' + ' ' + 'from url ' + ' ' + url_id
                    self.logger.info("Delete all data test pass")
                    self.verificationErrors.append(test_pass)



    def test_update(self, ex_response=None, data="None", header=None, http_address=None, files=None, timeout=None, id_number=None):



        if files is None:
            files  = self.files_out
        if timeout is None:
            timeout = self.timeout
        with open(files) as json_file:
                 files = json.load(json_file)


        self.logger.info("JSON DATA: %s" % files)
        url = "%s/%s" % (self.BASE_URL, http_address)



        url_id = url + '/' + str(id_number)
        response, timeout_out, delay_by = self.rest_yellowdog.put_files_request(url_id, timeout, files)

        self.logger.info("RESPONSE: %s %s %s" % (response, timeout_out, delay_by))

        if response is None:
                    failed = 'ERROR Update :' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'ERROR Fetch  ' + '' + 'TYPE: Status code is None from url ' + url_id
                    self.verificationErrors.append(failed)
        elif response.HTTP_CODE != ex_response:

                    print("Status code returned: %s meaning (%s); expected: %s (%s)" % (
                        response, HttpCodes.HTTP_CODEs[response.HTTP_CODE], ex_response,
                        HttpCodes.HTTP_CODEs[ex_response]))
                    m = HttpCodes.HTTP_CODEs[response.HTTP_CODE]
                    failed = 'ERROR Update :' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + 'TYPE: Wrong status code from' + ' ' + 'url address' + ' ' + url_id + ' ' + 'Expected value:' + str(
                        ex_response) + ' ' + 'Actuale value:' + ' ' + ' ' + str(response.HTTP_CODE)
                    self.verificationErrors.append(failed)

        elif timeout_out is True:
                    failed = 'ERROR Update :' + 'TIME:' + datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'TYPE: Timeout exceed' + ' ' + str(delay_by) + ' ' + 'from url ' + url_id
                    self.verificationErrors.append(failed)
                    self.logger.info("RESPONSE CODE OPEN POSITION: %s" % response.HTTP_CODE)
        else:
                    test_pass = datetime.datetime.now().strftime(
                        self.fmt) + ' ' + 'Update test  passed ' ' ' + 'TYPE: Timeout limit pass, Function, Correct status code returned, Server up and running' + ' ' + 'from url ' + ' ' + url_id
                    self.logger.info("Delete all data test pass")
                    self.verificationErrors.append(test_pass)








    def Kill(self):
        """
        Delete the Yellowdog instance
        """

        with open('report.txt', 'w') as filehandle:
            for listitem in self.verificationErrors:
                filehandle.write('%s\n' % listitem)
        del self.rest_yellowdog


if __name__ == "__main__":

     test = TestYellowDog('startUP', acc_type="nonesecure", timeout = 0.006, files_out="json_out.txt")
     test.startUP()
     test.test_create_account(ex_response = 200, http_address = "contacts", timeout = 0.2)
     test.test_fetch_all_data(ex_response = 200, http_address = "contacts", timeout = 0.2)
     test.test_fetch_by_id(ex_response = 200, http_address = "contacts", timeout = 0.2, id_number='6015fe9ab6cc125f02a29f9a')
     test.test_fetch_by_id_all(ex_response = 200, http_address = "contacts", timeout = 0.2, )
     test.test_delete(ex_response=200, http_address="contacts", timeout=0.2, id_number='6015fe67b6cc125f02a29f99')
     test.Kill()
     #PUT request does't work in normal or threading implementation
     #test.test_update(ex_response=200, http_address="contacts", timeout=0.2, id_number='6015fd89b6cc125f02a29f97')

