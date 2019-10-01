import pytest

from appsessionbase.test_calculatorbase import TestCalculatorBase
from appium.webdriver import WebElement

class TestElementEnabled(TestCalculatorBase):



    def test_getElementEnabledState(self):

        storeMemoryButton :WebElement  = self.session.find_element_by_accessibility_id('memButton')
        assert storeMemoryButton is not None

        clearMemoryButton :WebElement = self.session.find_element_by_accessibility_id('ClearMemoryButton')
        assert clearMemoryButton is not None

        assert storeMemoryButton.is_enabled() == True

        # Clear memory to disable clearMemoryButton (button could initially be already disabled)
        clearMemoryButton.click()
        assert clearMemoryButton.is_enabled() == False

        # Store memory to enable clearMemoryButton
        storeMemoryButton.click()
        assert storeMemoryButton.is_enabled() == True

        # Clear memory again to re-disable clearMemoryButton
        clearMemoryButton.click()
        assert clearMemoryButton.is_enabled() == False








