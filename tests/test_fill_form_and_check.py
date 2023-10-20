from selene import browser, be, have
import os.path

def test_fill_form_and_check():
    #Открыть браузер
    browser.open('/')

    #Заполнение формы
    browser.element('.practice-form-wrapper').should(be.visible)
    browser.element('#firstName').should(be.blank).type('Zukhra')
    browser.element('#lastName').should(be.blank).type('Nurmanova')
    browser.element('#userEmail').should(be.blank).type('zukhra.nurmanova@gmail.com')
    browser.element('#genterWrapper').should(be.existing)
    browser.element('label[for=gender-radio-2]').should(be.existing).click()
    browser.element('#userNumber').should(be.blank).type('7017781810')
    browser.element('#dateOfBirthInput').should(be.existing).click()
    browser.element('.react-datepicker').should(be.visible)
    browser.element('.react-datepicker__month-select').click().element('[value="9"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1988"]').click()
    browser.element('[class = "react-datepicker__day react-datepicker__day--010"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Computer').press_enter()
    browser.element('#hobbiesWrapper').should(be.visible)
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element('.form-file').should(be.visible)
    browser.element('#uploadPicture').send_keys(os.path.abspath('animation.gif'))
    browser.element('#currentAddress').should(be.blank).type('Almaty, st.Dostyk 43')
    browser.element('#stateCity-wrapper').should(be.visible)
    browser.element('#state').should(be.visible)
    browser.element('#react-select-3-input').should(be.blank).type('D').press_enter()
    browser.element('#city').should(be.visible)
    browser.element('#react-select-4-input').should(be.blank).type('A').press_enter()
    browser.element('#submit').should(be.visible).press_enter()

    #Проверить введенные данные
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Zukhra Nurmanova',
        'zukhra.nurmanova@gmail.com',
        'Female',
        '7017781810',
        '10 October,1988',
        'Computer Science',
        'Reading',
        'animation.gif',
        'Almaty, st.Dostyk 43',
        'Uttar Pradesh Agra'
        ))





