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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


@step('Open "{url}" url')
def open_url(context, url):
    if context.browser == "Chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        context.driver.maximize_window()
        context.driver.get(url)
    elif context.browser == "Firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--private")
        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                           options=firefox_options)
        context.driver.maximize_window()
        context.driver.get(url)
    else:
        assert False, "Unsupported browser " + context.browser


@step('Wait for "{timeout}" seconds')
def wait_sec(context, timeout):
    sleep(int(timeout))


@step('Page contains element "{xpath}"')
def page_contains_element(context, xpath):
    # element = context.driver.find_elements(By.XPATH, f"{xpath}")
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"


@step('Click on element "{xpath}"')
def click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"
    element.click()


@step('Type "{text}" in field "{xpath}"')
def type_in(context, text, xpath):
    elements = context.driver.find_elements(By.XPATH, f"{xpath}")
    assert elements, f"Element with xpath {xpath} is not found"
    elements[0].send_keys(text)


@step("Get weather in {city}")
def step_impl(context, city):
    temperature = get_weather(city)
    print(f"Temperature in {city}: {temperature} C")


@step('Open "{env}" environment')
def open_env(context, env):
    environments = {
        'prod': 'https://lifetwig.com/',
        'staging': 'https://test.sugaringfactory.com/index.php?route=account%2Flogin',
        'dev': 'development.lifetwig.com',
        'uat': 'uat.lifetwig.com',
        'sug_main': 'https://test.sugaringfactory.com/',
        'sug_login': 'https://test.sugaringfactory.com/index.php?route=account%2Flogin'
    }

    open_url(context, environments[env])


@step('Verify "{page_name}" page is exists')
def verify_page_exists(context, page_name):
    pages = {
        'login': "//div[contains(text(), 'Sign You In')]",
        'app': "//div[contains(@class, 'left-panel_user_info_card')]",
        'suga_login': "//h2[contains(text(), 'Returning Customer')]",
        'sug_forgot_pass': "//a[contains(text(), 'Forgotten Password')]",
        'app_sugar': "//a[contains(text(), 'Edit Account')]"
    }
    page_contains_element(context, pages[page_name])

    # switch to link Forgotten Password
    if page_name == 'sug_forgot_pass':
        click_element(context, "//a[contains(text(), 'Forgotten Password')]")


@step('Login as "{role}"')
def step_impl(context, role):
    credentials = {
        'admin': ('pcs.automationclass+10@gmail.com', '!Qwerty7890'),
        'tester': ('timkotimofeytest@gmail.com', '12345'),
        'user': ('qwertyuiop@yahoo.com', 'Sotirov1!'),
        'tester@artem': ('testforlifetwig.com@gmail.com', ''),
    }

    if role == 'admin':
        type_in(context, credentials[role][0], "//input[@id='login_email']")
        type_in(context, credentials[role][1], "//input[@id='login_password']")
        click_element(context, "//span[text()='Login']")
    elif role == 'tester':
        type_in(context, credentials[role][0], "//input[@name='email']")
        type_in(context, credentials[role][1], "//input[@name='password']")
        click_element(context, "//div[@class='login-buttons']/a[@class='button-cont-right']")

    elif role == 'tester@artem':
        type_in(context, credentials[role][0], "//input[@name='email']")
        sleep(int(3))
        click_element(context, "//span[contains(text(), 'Continue')]")


@step("Login with following credentials")
def login_with_cred(context):
    for row in context.table:
        if row['element'] == 'login':
            xpath = "//input[@id='login_email']"
        else:
            xpath = "//input[@id='login_password']"
        type_in(context, row['value'], xpath)
    click_element(context, "//span[text()='Login']")