import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("../utilities/logfile.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        # logger.debug("A debug statement is executed")
        # logger.info("information statement")
        # logger.warning("something is in warning mode")
        # logger.error("error occurred")
        # logger.critical("critical blocking issue")
        return logger

    def verifyLinkPresence(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))

    def selectByVisibleText(self,locator,text):
        dropDown = Select(locator)
        dropDown.select_by_visible_text(text)