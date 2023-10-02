import pytest
from selene import browser

@pytest.fixture
def open_browser():
    browser.config.window_height = 1200
    browser.config.window_width = 1400

    yield

    print("По запросу ничего не найдено")