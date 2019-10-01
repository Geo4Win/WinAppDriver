
import pytest
from appium import webdriver
from .commontestsettings import CommonTestSettings
from .webdriverapiextensions import findCalculatorTitleByAccessibilityId, dismissAlarmDialogIfThere

class TestCalculatorBase():
    session = None

    def setup_class(self):
        desired_caps = {}
        desired_caps["app"] = CommonTestSettings.CalculatorAppId

        self.session = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    def teardown_class(self):
        print("teardown_class called once for the class")
        self.session.quit()
    def test_findCalculatorTitleByAccessibilityId(self):
        elem = findCalculatorTitleByAccessibilityId(self.session)


class TestAlarmClock():
    session = None
    def setup_class(self):
        desired_caps = {}
        desired_caps['app'] = CommonTestSettings.AlarmClockAppId
        self.session = webdriver.Remote(command_executor='http://127.0.0.1:4723',
                                        desired_capabilities= desired_caps)

    def teardown_class(self):
        self.session.quit()

    def test_dismissAlarmDialogIfThere(self):
        dismissAlarmDialogIfThere(self.session)
