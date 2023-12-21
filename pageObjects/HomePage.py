from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH,"//a[text()='Shop']")
    nameField = (By.NAME,"name")
    emailField = (By.CSS_SELECTOR,"[name='email']")
    gender = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.CSS_SELECTOR,"[value='Submit']")
    msg = (By.CSS_SELECTOR,".alert.alert-success.alert-dismissible")

    def shopItems(self):
        self.driver.find_element(*self.shop).click()
        cp = CheckoutPage(self.driver)
        return cp

    def formFill(self,nm,em):
        self.driver.find_element(*self.nameField).send_keys(nm)
        self.driver.find_element(*self.emailField).send_keys(em)

    def submit_form(self):
        self.driver.find_element(*self.submitBtn).click()
        return self.driver.find_element(*self.msg).text

    def getGender(self):
        return self.driver.find_element(*self.gender)
