import pytest
from selene import browser, have


"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(scope='function', autouse=False, params=[(1366, 768), (1920, 1080)])
def desktop_browser(request):
    browser.config.window_width, browser.config.window_height = request.param

    yield

    browser.quit()


@pytest.fixture(scope='function', autouse=False, params=[(320, 568), (390, 844)])
def mobile_browser(request):
    browser.config.window_width, browser.config.window_height = request.param

    yield

    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('https://github.com')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(mobile_browser):
    browser.open('https://github.com')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
