import unittest
from logger import logger
from BssWebTestChallenge import BssWebTestChallenge
import time

class BssTestCase(unittest.TestCase):

    #Challenging DOM  test. host is address of remote server. Need to run hub and node 

    def __init__(self, testname,
                 host='172.18.0.1',
                 browser_type='Chrome',
                 website_under_test='https://the-internet.herokuapp.com',
                 action_button = 'button alert',
                 exp_title = 'The Internet'):



                 self.logger = logger(self.__class__.__name__)
                 self.logger.info("__init__() called")
                 super(BssTestCase, self).__init__(testname)
                 self.logger.info("testname: %s" % testname)
                 self.test_items = ['button', 'button alert', 'button success']
                 self.host = host
                 self.browser_type = browser_type
                 self.website_under_test = website_under_test
                 self.button = action_button
                 self.base = None
                 self.exp_title = exp_title

                 self.startUP()



    #set the test environment Create instanse of BssWebTestChalenge. 
    def startUP(self):
                    self.base = BssWebTestChallenge(host=self.host, browser_type=self.browser_type ,
                                           website_under_test=self.website_under_test)

                    self.logger.info("Creating new instance of base class")


    def tearDown(self):
           del self.base






    #run test cases 1.: checking website correct by title, select test page, collect ids in dict, press red button, collect ids in dic, run compare, if true  test pass. 
    #Failed conditions: 1.Wrong page selected. 2.  List of test items ids return empty  or some missing. 3. Problem pressing red button 4. Ids did not change after red button pressed
                      
 

    def test_verify_correctness(self):
        kk = []
        
        dic = {}
        gg = []
        dic2 = {}
        xpath = None
        self.logger.info("Start running test")
        title_corect = self.base.open(exp_title = self.exp_title)
        self.assertEqual(True, title_corect, msg = 'Title is not correct. Wrong Website')
        page_correct= self.base.select_page(page = "Challenging DOM")
        self.assertEqual(True, page_correct,msg = 'Challenge Dom page not found')
        time.sleep(5)


        for i in range(len(self.test_items)):
            xpath = "//div[contains(@class,'row')]/div[contains(@class,'large-12 columns large-centered')]/div[contains(@class, 'large-2 columns')]/a[contains(@class, '%s')]" % \
                    self.test_items[i]
            state = self.base.find_element_by_xpath(xpath)
           
            if state == False:
               self.assertEqual(True, state, msg='List of test items ids return empty  or some missing')
            
            kk.append(self.base.find_element_by_xpath(xpath))
        
       
               
        #populating dictionary with ids and corresponding key names     
        for i in range(len(kk)):
                self.logger.info("Save state of ids  %s  ---- %s:"  % (self.test_items[i], kk[i]))
                dic[self.test_items[i]] = kk[i]

        xpath = "//div[contains(@class,'row')]/div[contains(@class,'large-12 columns large-centered')]/div[contains(@class, 'large-2 columns')]/a[contains(@class, '%s')]"  %   self.button
        state = self.base.click_element_by_xpath(xpath)
        self.assertEqual(True, state, msg='Problem pressing red button')


        time.sleep(3)
        #get ids again afer red button pressed
        for i in range(len(self.test_items)):
            xpath = "//div[contains(@class,'row')]/div[contains(@class,'large-12 columns large-centered')]/div[contains(@class, 'large-2 columns')]/a[contains(@class, '%s')]" % \
                    self.test_items[i]
            state=gg.append(self.base.find_element_by_xpath(xpath))
            if state == False:
               self.assertEqual(True, state, msg='List of test items ids return empty  or some missing after red button pressed')

        

        for i in range(len(gg)):
            self.logger.info("Populating new dictionary with items:ids and key:class names %s  ---- %s:" % (self.test_items[i], gg[i]))
            dic2[self.test_items[i]] = gg[i]


        self.logger.info("Comparing states of ids after red button was pressed with states before")
        if dic == dic2:
            state = False
        else:
            state = True

        self.assertEqual(True, state, msg='Ids did not change after red button pressed. Test failed')

if __name__ == '__main__':
    unittest.main()
