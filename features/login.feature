Feature: User login Page
 These scenarios will validate the user login in positive and negative flows.

    Scenario: Login Page message

        Given the user access the Login page
        Then the login label message should be "Login with your Account"

    @teste
    Scenario: Log in with valid credentials

        Given the user types a valid username and password
            | username | password |
            | testuser | pl123    |
        When user clicks on Log in button
        Then the user details page should be displayed


    Scenario: Log in with an invalid username with correct password

        Given the user types an invalid username with a valid password
            | username | password |
            | user111  | pl123    |
        When user clicks on Log in button
        Then a pop-up containing the message "There was a problem logging in: Login/Password is incorrect" should be displayed 
        And the log in should fail


    Scenario: Log in with an invalid password with correct username

        Given the user types a valid username with an invalid password
            | username |    password    |
            | testuser | testinghehe    |
        When user clicks on Log in button
        Then a pop-up containing the message "There was a problem logging in: Login/Password is incorrect" should be displayed
        And the log in should fail

    Scenario Outline: Log in with empty Fields
    
        Given the user types <username> and <password>
        When user clicks on Log in button
        Then a pop-up containing the warning message "Please input your username." should be displayed
       
        
        Examples:
            | username  |   password    |
            |           |   123asdas    |
            |  123asdas |               |
            |           |               |

 

