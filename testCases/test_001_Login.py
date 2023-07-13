import datetime
import pytest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import os

class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = logGen.loggen()  # Logger

    user = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_login(self,setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"/screenshots/"+"Login"+datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".png")
            self.driver.close()
            assert False

        self.logger.info("******* End of test_002_login **********")
