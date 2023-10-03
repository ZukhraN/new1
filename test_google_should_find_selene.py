from selene.support.shared import browser
from selene import be, have


def test_find_in_the_browser(open_browser):

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))

def test_new_find(open_browser):

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('bcbvjcjnxjjnvsjnnnxnkcm').press_enter()
    browser.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))

