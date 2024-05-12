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
