from .utility import Utility
from .commontestsettings import CommonTestSettings, ErrorStrings
from selenium.webdriver.common.keys import Keys

from appium import webdriver
import pytest
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestEdgeBase():
    session : webdriver.Remote = None
    touchScreen  = None
    startingPageTitle = None
    maxNavigationHistory = 5

    def setup_class(cls):
        logger.info('\n=> setup class')
        # lunch Edge browser app if it is not yet launched
        if not cls.session or not Utility.currentWindowIsAlive(cls.session): # not cls.touchScreen
            # cleanup leftover objects from previous test if exists
            #cls.teardown_class()
            cls.teardown()

            # launch the Edge browser app
            cls.session = Utility.createNewSession( CommonTestSettings.EdgeAppId, "-private")
            cls.session.implicitly_wait(1000)
            assert cls.session is not None
            assert cls.session.session_id is not None

            # todo initialize touch screen object
            # cls.touchScreen =
            # assert cls.touchScreen is not None
        # track the Edge starting page title to be used to initialize all test cases
        import time
        time.sleep(1)
        cls.startingPageTitle = cls.session.title

        # handle Edge restored state by starting fresh
        if cls.startingPageTitle.startswith('Start fresh and '):
            try:
                cls.session.find_element_by_xpath('//Button[@Name="Start fresh "]').click()
                time.sleep(3)
                cls.startingPageTitle = cls.session.title
            except Exception as e:
                pass
                #logger.info(e)


    def teardown_class(cls):
        logger.info('\n=> teardown_class')
        cls.teardown()

    @classmethod
    def teardown(cls):
        logger.info('\n=> teardown()')
        cls.touchScreen = None
        # close the app and delete the session
        if cls.session is not None:
            cls.closeEdge(cls.session)
            cls.session.quit()
            cls.session = None

    @staticmethod
    def closeEdge(edgeSession: webdriver.Remote):
        logger.info('\n=> closeEdge')
        try:
            edgeSession.close()
            currentHandle = edgeSession.current_window_handle #This should throw if the window is closed successfully

            # when the Edge window remains open because of multiple tabs are open,
            # attempt to close modal dialog
            closeAllButton = edgeSession.find_element_by_xpath('//Button[@Name="Close all"]')
            closeAllButton.click()
        except Exception as e:
            pass
            #logger(e)


    def setup_method(self):
        logger.info('\n=> setup_method')
        # Restore Microsoft Edge to the main page by navigating the browser back in history
        for i in range(self.maxNavigationHistory):
            if self.session.title == self.startingPageTitle :
                logger.info('--> return')
                return
            else:
                logger.info('--> back')
                self.session.back()
        assert self.session is not None

    @classmethod
    def getStaleElement(cls) ->webdriver.WebElement:
        assert cls.session is not None
        logger.info('\n=> getStaleElement()')
        staleElement : webdriver.webelement = None
        keys = Keys.ALT +'d' + Keys.ALT + CommonTestSettings.EdgeAboutTabsURL + Keys.ENTER
        cls.session.find_element_by_accessibility_id('addressEditBox').send_keys()
        import time
        time.sleep(2)
        originalTitle = cls.session.title
        assert originalTitle is not None

        # navigate to Edge about:flags page
        keys = Keys.ALT + 'd' + Keys.ALT + CommonTestSettings.EdgeAboutFlagsURL + Keys.ENTER
        cls.session.find_element_by_accessibility_id('addressEditBox').send_keys(keys)
        time.sleep(3)
        assert originalTitle != cls.session.title

        # save a reference to Reset all flags button on the page and navigate back to home
        staleElement = cls.session.find_element_by_accessibility_id('ResetAllFlags')
        assert staleElement is not None
        cls.session.back()
        time.sleep(3)
        assert originalTitle == cls.session.title

        return staleElement


class TestEdgeBase_UT(TestEdgeBase):
    def test_one(self):
        elem = self.getStaleElement()





