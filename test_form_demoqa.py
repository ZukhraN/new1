import pytest
from selene.support.shared import browser
from selene import be, have

def test_find(open_browser):
    browser.open('https://demoqa.com/text-box')
    browser.element('#userName').type('Nurmanova')
    browser.element('#userEmail').type('zukhra.nurmanova@gmail.com')
    browser.element('#currentAddress').type('Almaty')
    browser.element('#permanentAddress').type('Almaty')
    browser.element('#submit').click()

    browser.element('#output').should(be.visible)
    browser.element('#name').should(have.text('Nurmanova'))
    browser.element('#email').should(have.text('zukhra.nurmanova@gmail.com'))
    browser.element('#output #currentAddress').should(have.text('Almaty'))
    browser.element('#output #permanentAddress').should(have.text('Almaty'))





