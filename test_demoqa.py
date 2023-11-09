from selene import have
from selene.support.shared import browser

browser.config.timeout = 10
def open_web_tables():
    browser.open('https://demoqa.com/text-box')
    browser.element('div.element-list.collapse.show > ul > li#item-3').click()
def fill_form():
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Vasil')
    browser.element('#lastName').type('Pupkin')
    browser.element('#userEmail').type('VasilBatyakovich@mail.ru')
    browser.element('#age').type('99')
    browser.element('#salary').type('99')
    browser.element('#department').type('Department of dog affrairs')
    browser.element('#submit').click()
def search_created_user():
    browser.element('#searchBox').type('Vasil').press_enter()
    browser.element('div.rt-td').should(have.text('Vasil'))
def test_add_user_in_table():
    open_web_tables()
    fill_form()
    search_created_user()
