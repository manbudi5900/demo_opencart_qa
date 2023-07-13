import time
from Pages.AccountRegistrationPage import AccountRegistrationPage
from Pages.HomePage import HomePage
from utilities import randomeString
import os

from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class Test_001_AccountReg:
    baseUrl = ReadConfig.getApplicationURL()
    logger = logGen.loggen()

    def test_account_reg(self, setup):
        self.logger.info("**test 001 account registrasi start**")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.logger.info("Launching aplikasi")
        self.driver.maximize_window()


        self.hp = HomePage(self.driver)
        self.logger.info("klik my account -> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("Input data customer")

        self.regpage = AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Don")
        self.email = randomeString.random_string_generator()+"@gmail.com"
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("12345678")

        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        time.sleep(5)
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration passed!")

            assert True
            self.driver.close()

        else:
            self.logger.error("Account registration failed!")
            self.driver.save_screenshot("test_account_registation.png")
            self.driver.close()

            assert False

        self.logger.info("**test 001 account registrasi end**")



