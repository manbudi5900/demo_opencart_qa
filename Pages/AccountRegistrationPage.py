from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import time
from selenium.common.exceptions import NoSuchElementException
from utilities.customLogger import logGen


class AccountRegistrationPage(BasePage):
    TXT_FIRST_NAME = (By.NAME, "firstname")
    TXT_LAST_NAME = (By.NAME, "lastname")
    TXT_EMAIL = (By.NAME, "email")
    TXT_PASSWORD = (By.NAME, "password")
    TXT_NEWS_LATTER = (By.NAME, "newsletter")
    BTN_CONTINUE = (By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/button")
    TXT_TERM= (By.NAME, "agree")
    TXT_MSG = (By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")



    def __init__(self, driver):
        self.driver = driver
    def setFirstName(self, name):
        self.input_element(self.TXT_FIRST_NAME, name)
    def setLastName(self, name):
        self.input_element(self.TXT_LAST_NAME, name)
    def setEmail(self, email):
        self.input_element(self.TXT_EMAIL, email)
    def setPassword(self, password):
        self.input_element(self.TXT_PASSWORD, password)
    def setPrivacyPolicy(self):
        self.click_element(self.TXT_TERM)
    def clickContinue(self):
        self.click_element(self.BTN_CONTINUE)
    def getconfirmationmsg(self):
        try:
            return self.get_element_text(self.TXT_MSG)
        except:
            None