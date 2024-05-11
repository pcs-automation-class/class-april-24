Feature: Lifetwig tests

  Scenario: Login with happy path
    Given Open "prod" environment
    Then Verify "login" page is exists
    Then Login as "admin"
    Then Wait for "2" seconds
    Then Verify "app" page is exists
    Then Wait for "2" seconds
