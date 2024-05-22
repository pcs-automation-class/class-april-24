# My first feature file
Feature: Login page tests

  Background: Login
    Given Open "qa" env
#    Then Wait for "2" seconds
    Then Page contains element "//div[contains(text(), 'Sign You In')]"
    Then Type "pcs.automationclass+10@gmail.com" in field "//input[@id='login_email']"
    Then Type "!Qwerty7890" in field "//input[@id='login_password']"
    Then Click on element "//span[text()='Login']"
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(@class, 'left-panel_user_info_card')]"

  Scenario: Login happy path
    Then Type "pcs.automationclass+10@gmail.com" in field "//input[@id='login_email']"
    Then Type "!Qwerty7890" in field "//input[@id='login_password']"
    Then Click on element "//span[text()='Login']"
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(@class, 'left-panel_user_info_card')]"


  Scenario: 1
    Given Open "https://lifetwig.com/" url
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(text(), 'Sign You In')]"
    Then Type "mytrialemail7890@gmail.com" in field "//input[@id='login_email']"
    Then Wait for "2" seconds
    Then Type "ForpyCharm312$" in field "//input[@id='login_password']"
    Then Wait for "2" seconds
    Then Click on element "//span[text()='Login']"
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(@class, 'left-panel_user_info_card')]"
    Then Wait for "2" seconds
    Then Click on element "//button[@class='left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='auth_auth_logo__36DCJ']"
    Then Wait for "2" seconds

  Scenario: Sign Up
    Given Open "https://lifetwig.com/" url
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(text(), 'Sign You In')]"
    Then Click on element "//a[@href="/registration"]"
    Then Wait for "2" seconds
    Then Type "Adriana" in field "//input[@id="registration_firstName"]"
    Then Type "Sotirov" in field "//input[@id="registration_lastName"]"
    Then Type "qwertyuiop@yahoo.com" in field "//input[@id='registration_email']"
    Then Wait for "2" seconds
    Then Type "Sotirov1!" in field "//input[@id='registration_password']"
    Then Wait for "2" seconds
    Then Click on element "//input[@type='checkbox']/parent::span"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'primary auth_register_form_button')]/parent::div"
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(@class,'registration-confirm_form_message')]"
    And Click on element "//button[./span[text()='Continue']]"


#  Scenario: Getr weather in Miami
#    Given Get weather in Chicago

  Scenario: Playing with the Privacy
    Then Type "pcs.automationclass+10@gmail.com" in field "//input[@id='login_email']"
    Then Type "!Qwerty7890" in field "//input[@id='login_password']"
    Then Click on element "//span[text()='Login']"
    Then Wait for "2" seconds
    Then Page contains element "//div[contains(@class, 'left-panel_user_info_card')]"
    Then Click on element "//a[@href='/settings']"
    Then Wait for "1" seconds
    Then Click on element "//div[contains(@class, 'settings_setting_container__1Syua')]//p[contains(text(), 'About information')]/ancestor::div[@class='settings_setting_container__1Syua']//div[contains(@class, 'ant-select-selector')]"
    Then Wait for "1" seconds
    Then Click on element "//div[@class='ant-select-item-option-content'][text()='Only Me']"
    Then Wait for "1" seconds

  Scenario: Toggle switcher
    Then Click on element "//a[@href='/settings']"
    Then Click on element "//a[@href='/settings/notifications']"
    Then Wait for "2" seconds
    Then Click on element "//button[@role='switch'][./parent::div[.//p[text()='Password change']]]"
    Then Wait for "2" seconds

  Scenario Outline: Toggle every switcher
    Then Click on element "//a[@href='/settings']"
    Then Click on element "//a[@href='/settings/notifications']"
    Then Wait for "1" seconds
    Then Click on element "<switcher_xpath>"
    Then Wait for "1" seconds

    Examples:
      | switcher_xpath                                                                   | state |
      | //button[@role='switch'][./parent::div[.//p[text()='Password change']]]          | On    |
      | //button[@role='switch'][./parent::div[.//p[text()='Connection accepted']]]      | On    |
      | //button[@role='switch'][./parent::div[.//p[text()='Birthdays']]]                | Off   |
      | //button[@role='switch'][./parent::div[.//p[text()='Likes, comments & shares']]] | On    |
