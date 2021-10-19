
from browser import Browser
from util    import Util


class LoginSelector(object):

    INPUT_USERNAME      = '[id="normal_login_username"]'
    INPUT_PASSWORD      = '[id="normal_login_password"]'
    
    LABEL_LOGIN_ERROR   = '[class="error-message"]'
    LABEL_LOGIN_EMPTY   = '[class="ant-form-explain]' 

    BUTTON_LOGIN        = '[class="ant-btn login-form-button ant-btn-primary"]'
    
    HEADER_WELCOME      = '[class="Header_Logo__3CSiC"]'



class LoginPage(Browser):

    util = Util ()


    def access_page(self, url):
        
        self.driver.get(url)

    def click_login_button(self):
        
        button = self.util.get_element(LoginSelector.BUTTON_LOGIN)
        button.click()

    def send_keys_username(self, username):
        
        input_username = self.util.get_element(LoginSelector.INPUT_USERNAME)
        input_username.send_keys(username)

    def send_keys_password(self, pwd):

        input_pwd = self.util.get_element(LoginSelector.INPUT_PASSWORD)
        input_pwd.send_keys(pwd)

    def is_login_successfull(self):

        element = self.util.get_element(LoginSelector.HEADER_WELCOME)

        return element.is_displayed()
    
    def is_login_unsuccessfull(self):

        element = self.util.get_element(LoginSelector.LABEL_LOGIN_ERROR)

        return element.is_displayed()

    

        

        
        
      

        
