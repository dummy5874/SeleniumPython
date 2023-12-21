import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        driver = self.driver
        hp = HomePage(driver)
        cp = hp.shopItems()
        log.info("Navigated to products page")

        prods = cp.getCardTitle()
        log.info("Getting all products title")
        prodToAdd = "Blackberry"

        j=-1
        for i in prods:
            j += 1
            sr = i.text

            if sr == prodToAdd:
                cp.getAddToCart()[j].click()
        log.info("Added desired product in the cart")
        cp.navigateToCheckOut().click()
        log.info("Navigated to checkout page")
        cfmPage = cp.checkOutItemsPage()
        log.info("Navigated to purchase order page")

        cfmPage.enterCountry("ind")
        log.info("Entered country name")

        self.verifyLinkPresence()
        # wait = WebDriverWait(driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))

        cfmPage.selectCountry()
        cfmPage.checkTermsCond()

        cfmPage.clickPurchaseField()
        sp = cfmPage.getAlertMsg()

        assert "! Thank yu" in sp
        log.info("AlerSuccesst message is correct")