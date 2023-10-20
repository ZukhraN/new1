import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 668
    browser.config.window_height = 950
    browser.config.timeout = 2
    yield

    browser.quit()
