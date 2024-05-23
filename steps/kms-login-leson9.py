from time import sleep

from behave import step
from selenium import webdriver
# from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from api import get_weather


@step('Open "{url}" url')
def open_url(context, url):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get(url)


@step('Wait for "{timeout}" seconds')
def wait_sec(context, timeout):
    sleep(int(timeout))


@step('Page contains element "{xpath}"')
def page_contains_element(context, xpath):
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"


@step('Click on element "{xpath}"')
def click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"
    element.click()


@step('Type "{text}" in field "{xpath}"')
def type_in(context, text, xpath):
    element = context.driver.find_elements(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element[0].send_keys(text)


@step("Get weather in {city}")
def step_impl(context, city):
    temperature = get_weather(city)
    print(f"Temperature in {city}: {temperature} C")


@step('Open "{env}" environment')
def open_env(context, env):
    # create dictionary with env
    environments = {
        'prod': 'https://lifetwig.com/',
        'staging': 'staging.lifetwig.com',
        'dev': 'development.lifetwig.com',
        'uat': 'uat.lifetwig.com'
    }
    # call open url function
    open_url(context, environments[env])

@step('Verify "{page_name}" page exists')
def verify_page_exists(context, page_name):
    pages = {
        'login': "//div[contains(text(), 'Sign You In')]",
        'app': "//div[contains(@class, 'left-panel_user_info_card')]"
    }

    page_contains_element(context, pages[page_name])

@step('Login as "{role}"')
def step_impl(context, role):
    credentials = {
        'admin': ('makstester77@gmail.com', 'Kms_12345'),
        'sales': ('mytrialemail7890@gmail.com', 'ForpyCharm312$'),
        'user': ('qwertyuiop@yahoo.com', 'Sotirov1!')
    }

    type_in(context, credentials[role][0], "//input[@id='login_email']")
    type_in(context, credentials[role][1], "//input[@id='login_password']")
    click_element(context, "//span[text()='Login']")
