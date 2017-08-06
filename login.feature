Feature: User can login with username and password

    Scenario: run login test
      Given web page is opened
       When set username "autotest", password "111111" to fields and press Enter
       Then user can see his account page

