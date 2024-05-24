Feature: Lifetwig tests

  Scenario: Login with happy path
    Given Open "prod" environment
    Then Verify "login" page is exists
    Then Login as "admin"
#    Then Wait for "2" seconds
    Then Verify "app" page is exists
    Then Wait for "2" seconds

#  Scenario: Login with happy path Sugaring
#    Given Open "staging" environment
#    Then Verify "suga_login" page is exists
#    Then Wait for "2" seconds
#    Then Login as "tester"
#    Then Wait for "2" seconds
#    Then Verify "app_sugar" page is exists
#    Then Wait for "2" seconds
#
#  Scenario: Login with credentials
#    Given Open "prod" environment
#    Then Verify "login" page is exists
#    Then Login with following credentials
#      | element  | value                            |
#      | login    | pcs.automationclass+10@gmail.com |
#      | password | !Qwerty7890                      |
#    Then Set Notifications with following
#      | setting                  | state |
#      | Password change          | On    |
#      | Connection accepted      | On    |
#      | Birthdays                | Off   |
#      | Likes, comments & shares | Off   |
#    Then Verify "app" page is exists
#    Then Wait for "2" seconds
#
#  Scenario Outline:
#    Given Customers with following
#      | field_1    | field_2  |
#      | Name      | <names>  |
#      | Last Name | <lnames> |
#      | phone     | <phones> |
#      | email     | <emails> |
#
#    Examples:
#      | names | lnames | phones  | emails         |
#      | Alex  | Waine  | 8888888 | alex@gmail.com |
#      | Anna  | Waine  | 8899999 | anna@gmail.com |