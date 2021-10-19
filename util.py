
from browser import Browser



class Util(Browser):

    def get_element(self, css_selector):

        return self.driver.find_element_by_css_selector(css_selector)

    
        

      

    