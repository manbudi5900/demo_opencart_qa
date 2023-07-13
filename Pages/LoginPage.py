from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    txt_email_xpath =  (By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/div/form/div[1]/input")
    txt_password_xpath =  (By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/div/form/div[2]/input")
    btn_login_xpath =  (By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/div/form/button")
    msg_myaccount_xpath =  (By.XPATH,"//h2[text()='My Account']")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.input_element(self.txt_email_xpath, email)
    def setPassword(self, pwd):
        self.input_element(self.txt_password_xpath, pwd)
    def clickLogin(self):
        self.click_element(self.btn_login_xpath)
    def isMyAccountPageExists(self):
        try:
            return self.verify_element_displayed(self.msg_myaccount_xpath)
        except:
            return False

