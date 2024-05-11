Feature: Lifetwig tests
#
#  Scenario: Login with happy path
#    Given Open "prod" environment
#    Then Verify "login" page is exists
#    Then Login as "admin"
#    Then Wait for "2" seconds
#    Then Verify "app" page is exists
#    Then Wait for "2" seconds
#
Scenario: Login with happy path Sugaring
    Given Open "staging" environment
    Then Verify "suga_login" page is exists
    Then Wait for "2" seconds
    Then Login as "tester"
    Then Wait for "2" seconds
    Then Verify "app_sugar" page is exists
    Then Wait for "2" seconds