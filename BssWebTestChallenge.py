from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from logger import logger



#main selenium class use by the unit test cases. Basic functionalty . Only support firefox
class BssWebTestChallenge(object):

    def __init__(self, host=None, browser_type=None, website_under_test=None):


                self.browser_type = browser_type
                self.host = host
                self.website_under_test = website_under_test
                if  self.browser_type == "Chrome":
                    capOptions = webdriver.ChromeOptions()
		    try:
		       self.wd = webdriver.Remote(command_executor='http://%s:4444/wd/hub' % self.host, options = capOptions)
		    except ErrorInResponseException as err:
		           #print_error(err)
		           if "Reached error page" in str(err):
		               print_error("Unable to Navigate to URL:{}"\
		               "possibly because of the url is not valid".format(self.host))
	     
           
                else:
                    self.logger.info("Can be extended for IE, Opera and Firefox")
                self.wd.maximize_window()
                self.logger = logger(self.__class__.__name__)
                self.logger.info("__init__() called")


    def open(self,website_under_test = None, exp_title = None ):

                    title = None
                    if website_under_test == None:
                        website_under_test = self.website_under_test
                    self.wd.implicitly_wait(5)
                    self.wd.get(website_under_test)
                    title = self.wd.title
                    title = str(title)
                    self.logger.info("Title name and expected title name: %s -- %s" % (title, exp_title))

                    if title == exp_title:
                       return True
                    else:
                       return False





    def select_page_multilevel(self, page, linktext = None):
                    """
                    Navigate to  required destination. Two levels but can be extended..
                            """
                    try:
                        self.wd.find_element_by_link_text(page).click()
                        time.sleep(2)
                        if linktext is not None:
                            try:
                                wait = WebDriverWait(self.wd, 5)
                                wait.until(EC.element_to_be_clickable((By.LINK_TEXT, linktext)))
                                return self.wd.find_element_by_link_text(linktext).click()
                            except TimeoutException:
                                return False

                        time.sleep(4)
                    except NoSuchElementException:
                        return False

    def select_page(self, page, linktext = None):
                    """
                    Navigate to  required destination. Single level
                            """
                    try:

                        self.wd.find_element_by_link_text(page).click()
                        time.sleep(2)
                        return True
                    except NoSuchElementException:
                        return False

   

    def find_element_by_xpath(self, xpath):
                   try:    
                       return self.wd.find_element_by_xpath(xpath).id
                   except NoSuchElementException:
                       return False



    def confirm_text_onscreen(self, tag_name = None, exp_tag = None, exp_text = None, waiting = 1, el_pos = 0):

                    self.logger.info("Confirm text on screen function: %s -- %s --%s - %s - %s" % (tag_name, exp_tag, exp_text, waiting, el_pos))

                    try:
                        element = self.wd.find_elements_by_tag_name(tag_name)[el_pos]
                        element.click()
                        try:
                           WebDriverWait(self.wd, waiting).until(EC.presence_of_element_located((By.XPATH, "//{0}[contains(text(), '{1}')]".format(exp_tag, exp_text))))
                           return True
                        except TimeoutException:
                            return False
                    except NoSuchElementException:
                        return False


    def find_elements_by_tag_name(self, id_name):
                   try:
                       element = self.wd.find_elements_by_tag_name(id_name)[0]
                       element.click()
                   except NoSuchElementException:
                       return None


    def find_elements_by_tag_id(self, id_name):
        try:
           element = self.wd.find_elements_by_tag_name(id_name)
        except NoSuchElementException:
            return None



    def click_element_by_xpath(self, xpath):
                   try:
                       self.wd.find_element_by_xpath(xpath).click()
                       return True
                   except NoSuchElementException:
                       return False
    
    def find_element_by_classname(self, classname = None):

                   try:    
                      return self.wd.find_elements_by_class_name(classname)
                   except NoSuchElementException:
                       return None


    

   
                     

    def __del__(self):
        
        
        if self.wd is not None:
            self.wd.close()


