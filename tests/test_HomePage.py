import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getlogger()
        driver = self.driver
        hp = HomePage(driver)
        hp.formFill(getData["fname"],getData["email"])
        log.info("Entered First name and email to login into the application")
        self.selectByVisibleText(hp.getGender(),getData["gend"])
        log.info("Selected gender attribute")
        sr = hp.submit_form()
        log.info("Submitted form")
        assert "Success" in sr
        log.info("form is submitted successfully with correct message")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getExcelData("Testcase1"))
    def getData(self,request):
        return request.param

