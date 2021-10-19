import allure_commons
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure

class Browser(object):
   
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    
    def closeSession(self):
        self.driver.quit()
    
    
    def clearSession(self):

        self.driver.delete_all_cookies()
        self.driver.refresh()

    def attachmentScreenshoot(self, scenario):

        allure.attach(self.driver.get_screenshot_as_png(), name=scenario, attachment_type=AttachmentType.PNG)
    

    