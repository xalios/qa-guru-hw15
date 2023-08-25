import pytest
from selene import browser, have


"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


def is_mobile(width):
    return width < 1000


@pytest.fixture(
    scope='function',
    autouse=True,
    params=[(1366, 768), (1920, 1080), (400, 600)]
)
def browser_manager(request):
    browser.config.window_width, browser.config.window_height = request.param

    yield

    browser.quit()


def test_github_desktop():
    if is_mobile(browser.config.window_width):
        pytest.skip('Этот тест только для десктопа')
    browser.open('https://github.com')
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile():
    if not is_mobile(browser.config.window_width):
        pytest.skip('Этот тест только для мобильных устройств')
    browser.open('https://github.com')
    browser.element('.flex-1 button').click()
    browser.element("a[href='/login']").click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
