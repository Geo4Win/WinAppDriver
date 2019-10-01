import pytest
import time

from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains

from .commontestsettings import CommonTestSettings, ErrorStrings
from .utility import Utility
from .webdriverapiextensions import dismissAlarmDialogIfThere, findCalculatorTitleByAccessibilityId


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class TestAlarmClockBase():
    session : webdriver.Remote = None
    touchScreen = None
    alarmTabElement : webdriver.WebElement = None

    # UI elements attributes that differ between Alarms & Clock versions
    alarmTabAutomationId = None
    alarmTabClassName = None
    stopwatchTabAutomationId = None
    worldClockTabAutomationId = None

    def setup_class(cls):
        # launch Alarm & Clock application if it is not yet launched
        if not cls.session or not Utility.currentWindowIsAlive(cls.session) : # not touchScreen
            cls.teardown()

            cls.session = Utility.createNewSession(CommonTestSettings.AlarmClockAppId)
            assert cls.session is not None
            assert cls.session.session_id is not None

            # set implicit timeout to 2.5 seconds to make element search to retry
            # every 500ms for at most five times
            cls.session.implicitly_wait(2.5)

            # init touch screen object
            # touchScreen =
            # assert touchScreen is not None


    def teardown_class(cls):
        cls.teardown()

    @classmethod
    def teardown(cls):
        # cleanup remote touch screen object if initalized
        touchScreen = None
        #close the application and delete the session
        if cls.session != None:
            cls.session.quit()
            cls.session = None




    def setup_method(self):
        # attempt to go back to the main page in case Alarm & Clock app is started in EditAlarm view
        try :
            self.alarmTabElement = self.findAlarmTabElement()
        except Exception as e:
            self.dismissAddAlarmPage()
            self.alarmTabElement = self.findAlarmTabElement()

        assert self.alarmTabElement is not None
        if not self.alarmTabElement.is_selected():
            self.alarmTabElement.click()

        # different Alarm & Clock application version uses different UI elements
        if self.alarmTabElement.get_attribute('AutomationId') == 'AlarmButton':
            #latest version
            self.alarmTabClassName ='ListViewItem'
            self.alarmTabAutomationId ='AlarmButton'
            self.stopwatchTabAutomationId = 'StopwatchButton'
            self.worldClockTabAutomationId = 'ClockButton'

        else:
            # earlier version
            self.alarmTabClassName ='PivotItem'
            self.alarmTabAutomationId ='AlarmPivotItem'
            self.stopwatchTabAutomationId = 'StopwatchPivotItem'
            self.worldClockTabAutomationId = 'WorldClockPivotItem'

    def addAlarmEntry(self , alarmName : str):
        self.session.find_element_by_accessibility_id('AddAlarmButton').click()
        self.session.find_element_by_accessibility_id('AlarmNameTextBox').clear()
        self.session.find_element_by_accessibility_id('AlarmNameTextBox').send_keys(alarmName)
        self.session.find_element_by_accessibility_id('AlarmSaveButton').click()

    def deletePreviouslyCreatedAlarmEntry(self, alarmName: str):
        while True:
            try:
                alarmEntry = self.session.find_element_by_xpath(r'//ListItem[starts-with(@Name, \"{0}\")]'.format(alarmName))
                actions = ActionChains(self.session)
                actions.move_to_element(alarmEntry)
                actions.context_click(alarmEntry)
                actions.perform()
            except Exception as e:
                break



    def createStopwatchLapEntries(self, numberOfEntry : int):
        #navigate to stopwatch tab
        stopwatchPivotItem : webdriver.WebElement = self.session.find_element_by_accessibility_id(self.stopwatchTabAutomationId)
        stopwatchPivotItem.click()

        #reset stopwatch
        stopwatchResetButton :webdriver.WebElement= stopwatchPivotItem.find_element_by_accessibility_id('StopWatchResetButton')
        stopwatchPlayPauseButton :webdriver.WebElement = stopwatchPivotItem.find_element_by_accessibility_id('StopwatchPlayPauseButton')
        stopwatchResetButton.click()

        # collect lap entries
        stopwatchPlayPauseButton.click()
        stopwatchLapButton :webdriver.WebElement = stopwatchPivotItem.find_element_by_accessibility_id('StopWatchLapButton')
        for i in range( numberOfEntry):
            stopwatchLapButton.click()

        stopwatchPlayPauseButton.click()

    def getStaleElement(self):
        # open the add alarm page, locate the save button and click it to get a stale save button
        self.session.find_element_by_accessibility_id('AddAlarmButton').click()

        time.sleep(1)
        staleElement : webdriver.WebElement = self.session.find_element_by_accessibility_id('AlarmSaveButton')
        self.dismissAddAlarmPage()
        time.sleep(2)
        return staleElement

    def dismissAddAlarmPage(self):
        try:
            # press cancel button to dismiss any non main page
            self.session.find_element_by_accessibility_id('CancelButton').click()
        except Exception as e:
            # press back button if cancel button above somehow fail
            self.session.find_element_by_accessibility_id('Back').click()

            time.sleep(1)
            dismissAlarmDialogIfThere(self.session)

    def findAlarmTabElement(self):
        element : webdriver.WebElement = None
        try:
            # the latest Alarm & Clock applicat use a ListViewItem
            # with 'AlarmButton' automation id as the alarm tab selector
            element = self.session.find_element_by_accessibility_id('AlarmButton')
        except Exception as e:
            # the previsous version of Alarm & Clock app uses a PivotItem with
            # 'AlarmPivotItem' automation id as the alarm tab selector
            element = self.session.find_element_by_accessibility_id('AlarmPivotItem')
        return element


    def findAppTitleBar(self):
        element : webdriver.WebElement = None
        try:
            element = self.session.find_element_by_accessibility_id('AppName')
        except Exception as e:
            element = self.session.find_element_by_accessibility_id('TitleBar')

        return element



class TestAlarmClock_UT(TestAlarmClockBase):
    def test_zero(self):
        pass

    def test_one(self):
        elem = self.getStaleElement()










