from behave import * 
from pages.login_page import LoginPage, LoginSelector
from hamcrest import *

import parse

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


register_type(NullableString=parse_nullable_string)
loginPage       = LoginPage()
loginselector   = LoginSelector()


# Scenario: Log in with valid credentials
@given('the user types a valid username and password')
def step_impl(context):

    loginPage.access_page("http://localhost:3000/#/sign_in?last_page=")
    loginPage.send_keys_username("testuser")
    loginPage.send_keys_password("pl123")

@when('user clicks on Log in button')
def step_impl(context):
    
    loginPage.click_login_button()

@then('the user details page should be displayed')
def step_impl(context):
      
    assert_that(loginPage.is_login_successfull(), equal_to(True)) 
    


# Scenario: Log in with an invalid username with correct password
@given('the user types an invalid username with a valid password')
def step_impl(context):

    loginPage.access_page("http://localhost:3000/#/sign_in?last_page=")
    loginPage.send_keys_username("user111")
    loginPage.send_keys_password("pl123")


@then('a pop-up containing the message {} should be displayed')
def step_impl(context, strg):
    
    assert_that(loginPage.util.get_element(loginselector.LABEL_LOGIN_ERROR).text, equal_to(str(strg)[1:-1]))
    
    
@step('the log in should fail')
def step_impl(context):

    assert_that(loginPage.is_login_unsuccessfull(), equal_to(True))
    



# Scenario: Log in with an invalid password with correct username
@given('the user types a valid username with an invalid password')
def step_impl(context):

    loginPage.access_page("http://localhost:3000/#/sign_in?last_page=")
    loginPage.send_keys_username("testuser")
    loginPage.send_keys_password("testinghehe")



# Scenario: Log in with empty Fields
@given('the user types {username:NullableString} and {password:NullableString}')
def step_impl(context, username, password):

    loginPage.access_page("http://localhost:3000/#/sign_in?last_page=")
    loginPage.send_keys_username(username)
    loginPage.send_keys_password(password)

@then('a pop-up containing the warning message {} should be displayed')
def step_impl(context, strg):

    assert_that(loginPage.util.get_element(loginselector.LABEL_LOGIN_EMPTY).text, equal_to(str(strg)[1:-1]))







