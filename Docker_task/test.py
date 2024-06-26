import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set Chrome options
options = Options()
options.set_capability('selenoid:options',
                       {'enableVNC': True,
                        'browserName': 'chrome',
                        'version': '125',
                        'screenResolution': '1920x1080x24',
                        "enableLog": True})

url = 'https://duckduckgo.com'
valid_value = 'Innowise'
invalid_value = 'asdfghjklqwerty89'


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    # Start remote webdriver
    browser = webdriver.Remote(command_executor="http://10.131.33.67:4444/wd/hub", options=options)
    # browser = webdriver.Remote(command_executor="http://192.168.1.19:4444/wd/hub", options=options)
    browser.get(url)
    time.sleep(10)
    yield browser
    browser.quit()


def test_search_with_valid_values(browser_setup):
    browser_setup.find_element(By.ID, 'searchbox_input').send_keys(valid_value)
    browser_setup.find_element(By.CLASS_NAME, 'searchbox_searchButton__F5Bwq').click()
    assert browser_setup.find_element(By.XPATH, '//span[text()="Software Development Company | Innowise"]')


def test_search_with_invalid_values(browser_setup):
    browser_setup.get(url)
    browser_setup.find_element(By.ID, 'searchbox_input').send_keys(invalid_value)
    browser_setup.find_element(By.CLASS_NAME, 'searchbox_searchButton__F5Bwq').click()
    xpath = f'//*[contains(text(), "No results found for") and contains(., "{invalid_value}")]'
    assert browser_setup.find_element(By.XPATH, xpath)
