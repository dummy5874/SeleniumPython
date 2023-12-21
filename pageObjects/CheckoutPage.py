from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR,".card-title a")
    prodName = (By.XPATH,"div/h4")
    AddToCartBtn = (By.CSS_SELECTOR,".btn.btn-info")
    checkOut = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    checkOutItems = (By.CSS_SELECTOR, ".btn.btn-success")

    def getCardTitle(self):
        return self.driver.find_elements(*self.cardTitle)

    def getProdName(self):
        return self.driver.find_element(*self.prodName)

    def getAddToCart(self):
        return self.driver.find_elements(*self.AddToCartBtn)

    def navigateToCheckOut(self):
        return self.driver.find_element(*self.checkOut)

    def checkOutItemsPage(self):
        self.driver.find_element(*self.checkOutItems).click()
        cfmPage = ConfirmPage(self.driver)
        return cfmPage

