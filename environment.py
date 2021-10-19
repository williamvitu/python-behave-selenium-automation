from browser import Browser



def before_all(context):

    context.browser = Browser()
    

def after_all(context):

    context.browser.closeSession()
    

def after_scenario(context, scenario):
    
    context.browser.attachmentScreenshoot(scenario.name)
    context.browser.clearSession()
    
    