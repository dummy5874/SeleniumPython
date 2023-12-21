from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    countryField = (By.ID, "country")
    suggestionBox = (By.CLASS_NAME, "suggestions")
    Country = (By.LINK_TEXT, "India")
    checkTerms = (By.CSS_SELECTOR, "[for='checkbox2']")
    clickPurchase = (By.CSS_SELECTOR, "[value='Purchase']")
    alertMsg = (By.CLASS_NAME, "alert-success")

    def enterCountry(self,con):
        self.driver.find_element(*self.countryField).send_keys(con)

    def suggestBox(self):
        return self.suggestionBox

    def selectCountry(self):
        self.driver.find_element(*self.Country).click()

    def checkTermsCond(self):
        self.driver.find_element(*self.checkTerms).click()

    def clickPurchaseField(self):
        self.driver.find_element(*self.clickPurchase).click()

    def getAlertMsg(self):
        return self.driver.find_element(*self.alertMsg).text
