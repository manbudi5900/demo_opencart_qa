from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import time
from selenium.common.exceptions import NoSuchElementException


class HomePage(BasePage):
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"
    BTN_LOGIN =(By.LINK_TEXT, lnk_login_linktext)
    BTN_REGISTER =(By.LINK_TEXT, lnk_register_linktext)
    BTN_ACC = (By.XPATH, "//*[@id='top']/div[2]/div[2]/ul/li[2]/div/a")


    def __init__(self, driver):
        self.driver = driver
    def clickMyAccount(self):
        self.click_element(self.BTN_ACC)
    def clickRegister(self):
        self.click_element(self.BTN_REGISTER)
    def clickLogin(self):
        self.click_element(self.BTN_LOGIN)