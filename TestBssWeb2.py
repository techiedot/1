import unittest
from logger import logger
from BssWebTestChallenge import BssWebTestChallenge
import time


#Hello world test. Waiting and confirming item. host is address remote server. Need to run hub and node 
class BssTestCase(unittest.TestCase):

    def __init__(self, testname,
                 host='172.18.0.1',
                 browser_type='Chrome',
                 website_under_test='https://the-internet.herokuapp.com',
                 tag_name = "button",
                 exp_tag = 'h4',
                 exp_text = 'Hello World!',
                 action_button = 'button alert',
                 weblink = 'https://the-internet.herokuapp.com/challenging_dom',
                 exp_title = 'The Internet'):



                 self.logger = logger(self.__class__.__name__)
                 self.logger.info("__init__() called")
                 super(BssTestCase, self).__init__(testname)
                 self.logger.info("testname: %s" % testname)


                 self.test_items = ['button', 'button alert', 'button success']
                 self.host = host
                 self.browser_type = browser_type
                 self.website_under_test = website_under_test
                 self.tag_name = tag_name
                 self.exp_tag =  exp_tag
                 self.exp_text =  exp_text
                 self.button = action_button
                 self.weblink = weblink
                 self.base = None
                 self.exp_title = exp_title
                 self.startUP()


   #setting up test environment

    def startUP(self):
                    self.base = BssWebTestChallenge(host=self.host, browser_type=self.browser_type ,
                                           website_under_test=self.website_under_test)
                    self.logger.info("Creating new instance of base class")


    def tearDown(self):
           del self.base




    #check if website has correct title. step to subpage under test, press button, wait until item. If item is true test pass.
    
    #Failed conditions: 1.Wrong website selected. 2. Test page not found. 3. Problem pressing red button 4. Item could not be verify. 
    #Possible other test case - Timeout
                      
    def test_verify_correctness(self):
        state = self.base.open(exp_title=self.exp_title)
        self.assertEqual(True, state, msg='Title is not correct')
        state = self.base.select_page_multilevel("Dynamic Loading", "Example 2: Element rendered after the fact")
        time.sleep(5)
        self.assertIsNone(state, msg='Test page not found')
        state = self.base.confirm_text_onscreen(tag_name=self.tag_name, exp_tag=self.exp_tag, exp_text=self.exp_text)
        self.assertEqual(True, state, msg='Item could not be verify. Test failed ')






if __name__ == '__main__':
    unittest.main()
