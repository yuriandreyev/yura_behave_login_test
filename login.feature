Feature: User can login with username and password

    Scenario: run login test
      Given web page is opened
       When set username, password to fields and press Enter
       Then user can see his account page
       And browser should be closed
