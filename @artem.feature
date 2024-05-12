Feature: Sugaring tests

  Scenario: Forgotten Password  with happy path
    Given Open "sug_login" environment
    Then Wait for "2" seconds
    Then Verify "sug_forgot_pass" page is exists
    Then Wait for "2" seconds
    Then Login as "tester@artem"
