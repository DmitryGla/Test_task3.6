import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome")
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language= request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5) 
#все равно по дефолту будет запускаться chrome, но оставим эту строчку, чтобы не забывать
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser
    print("\nquit browser...")
    browser.quit()
    