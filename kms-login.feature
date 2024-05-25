# My first feature file
Feature: Login page tests

#  Background: Login
#    Given Open "https://www.lifetwig.com/login" url
#    Then Wait for "2" seconds
#    Then Page contains element "//div[text()='Let’s Sign You In']"
#    Then Type "*********77@gmail.com" in field "//input[@placeholder='Email Address']"
#    Then Wait for "2" seconds
#    Then Type "**********" in field "//input[@placeholder='Password']"
#    Then Wait for "2" seconds
#    Then Click on element "//button[@type='submit']"

  Scenario: Login happy path
    Given Open "https://www.lifetwig.com/" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester77@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='User']"
    Then Wait for "2" seconds
    Then Click on element "//p[text()='Logout']"
    Then Wait for "2" seconds

  Scenario: Login with wrong credentials
    Given Open "https://lifetwig.com/" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester7@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "Kms12345" in field "//input[@placeholder='Password']"
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='auth_auth_error__3IatI']"
    Then Wait for "2" seconds

  Scenario: Sign Up
    Given Open "https://www.lifetwig.com/" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Wait for "2" seconds
    Then Click on element "//a[@href='/registration']"
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Sign up']"
    Then Wait for "2" seconds
    Then Type "User" in field "//input[@placeholder='First Name']"
    Then Wait for "2" seconds
    Then Type "Second" in field "//input[@placeholder='Last Name']"
    Then Wait for "2" seconds
    Then Type "makstester77+5@gmail.com" in field "//input[@placeholder='Email address']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//span[@class='ant-checkbox']"
    Then Wait for "2" seconds
    Then Page contains element "//span[@class='ant-checkbox ant-checkbox-checked']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='registration-confirm_form_header__Jqe3y']"

  Scenario: Notifications1
    Given Open "https://www.lifetwig.com/login" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester77@gmail.com" in field "//input[@id='login_email']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@id='login_password']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='left-panel_user_info_card__YqAbG']"
    Then Wait for "2" seconds
    Then Click on element "//a[@href='/settings']/child::p"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='settings_header_container__2_F91']"
    Then Wait for "2" seconds
    Then Click on element "//a[@class='settings_header_element_inner__2io01'][text()='Notifications']"
    Then Wait for "2" seconds
    Then Page contains element "//a[@class='settings_header_element_inner__2io01 settings_header_element_active__1vKi3']"
    Then Wait for "2" seconds
    Then Click on element "//div[@class='settings_setting_container__1Syua' and .//p[text()='Password change']]//button[@role='switch']"
    Then Wait for "2" seconds
    Then Click on element "//div[@class='settings_setting_container__1Syua' and .//p[text()='Connection accepted']]//button[@role='switch']"
    Then Wait for "2" seconds
    Then Click on element "//div[@class='settings_setting_container__1Syua' and .//p[text()='Birthdays']]//button[@role='switch']"
    Then Wait for "2" seconds
    Then Click on element "//div[@class='settings_setting_container__1Syua' and .//p[text()='Likes, comments & shares']]//button[@role='switch']"
    Then Wait for "2" seconds

  Scenario: Notifications2
    Given Open "https://www.lifetwig.com/login" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester77@gmail.com" in field "//input[@id='login_email']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@id='login_password']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='left-panel_user_info_card__YqAbG']"
    Then Wait for "2" seconds
    Then Click on element "//a[@href='/settings']/child::p"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='settings_header_container__2_F91']"
    Then Wait for "2" seconds
    Then Click on element "//a[@class='settings_header_element_inner__2io01'][text()='Notifications']"
    Then Wait for "2" seconds
    Then Page contains element "//a[@class='settings_header_element_inner__2io01 settings_header_element_active__1vKi3']"
    Then Wait for "2" seconds
    Then Click on element "//button[@role='switch'][./parent::div[.//p[text()='Password change']]]"
    Then Wait for "2" seconds
    Then Click on element "//button[@role='switch'][./parent::div[.//p[text()='Connection accepted']]]"
    Then Wait for "2" seconds
    Then Click on element "//button[@role='switch'][./parent::div[.//p[text()='Birthdays']]]"
    Then Wait for "2" seconds
    Then Click on element "//button[@role='switch'][./parent::div[.//p[text()='Likes, comments & shares']]]"
    Then Wait for "2" seconds

  Scenario: Privacy
    Given Open "https://www.lifetwig.com/login" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester77@gmail.com" in field "//input[@id='login_email']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@id='login_password']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='left-panel_user_info_card__YqAbG']"
    Then Wait for "2" seconds
    Then Click on element "//a[@href='/settings']/child::p"
    Then Wait for "2" seconds
    Then Page contains element "//div[@class='settings_header_container__2_F91']"
    Then Wait for "2" seconds

  Scenario: Toggle switcher
    Given Open "https://www.lifetwig.com/login" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester77@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='User']"
    Then Click on element "//a[@href='/settings']/child::p"
    Then Wait for "2" seconds
    Then Click on element "//a[@class='settings_header_element_inner__2io01'][text()='Notifications']"
    Then Wait for "2" seconds
    Then Click on element "//button[@role='switch'][./parent::div[.//p[text()='Password change']]]"
    Then Wait for "2" seconds

  Scenario Outline: Toggle every switcher
    Given Open "https://www.lifetwig.com/login" url
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='Let’s Sign You In']"
    Then Type "makstester77@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Kms_12345" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[@type='submit']"
    Then Wait for "2" seconds
    Then Page contains element "//div[text()='User']"
    Then Click on element "//a[@href='/settings']/child::p"
    Then Wait for "2" seconds
    Then Click on element "//a[@class='settings_header_element_inner__2io01'][text()='Notifications']"
    Then Wait for "2" seconds
    Then Click on element "<switcher xpath>"
    Then Wait for "2" seconds

    Examples:
      | switcher xpath                                                                   | state |
      | //button[@role='switch'][./parent::div[.//p[text()='Password change']]]          | On    |
      | //button[@role='switch'][./parent::div[.//p[text()='Connection accepted']]]      | On    |
      | //button[@role='switch'][./parent::div[.//p[text()='Birthdays']]]                | Off   |
      | //button[@role='switch'][./parent::div[.//p[text()='Likes, comments & shares']]] | On    |

