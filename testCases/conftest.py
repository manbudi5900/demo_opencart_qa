import datetime
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os



@pytest.fixture()
def setup(browser):
   
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser.........")
    else:
        path ="/Users/macbook/Desktop/selenium/chromedriver"
        driver = ChromeService(executable_path=path)
        driver = webdriver.Chrome(service=driver)
        print("Launching chrome browser.........")
    return driver
def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"/reports/"+datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

