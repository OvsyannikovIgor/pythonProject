import pytest
from selene import be, have
from selene.support.shared import browser

browser.config.timeout = 10
@pytest.fixture()
def size_window():
    browser.driver.set_window_size(1920, 1080)
    yield
    browser.driver.set_window_size(720, 480)
    browser.open('https://animals.pibig.info/uploads/posts/2023-04/'
                 '1681420564_animals-pibig-info-p-koti-s-yazikom-zhivotnie-vkontakte-1.jpg')


def test_search_nothing(size_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ldfhlksdjhflksjhlksjfhglksjdfhgl').press_enter()
    browser.element('.card-section').should(have.text(' ничего не найдено. '))
