import pytest
from appium import webdriver
from .utility import Utility
from .commontestsettings import CommonTestSettings, ErrorStrings
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCalculatorBase(object):

    session: webdriver.Remote = None  # webdriver
    touchScreen = None
    header = None  # element

    def setup_class(cls):
        logger.info('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')


        if cls.session is None or cls.touchScreen is None:
            cls.session = Utility.createNewSession(CommonTestSettings.CalculatorAppId)

        try:
            cls.header = cls.session.find_element_by_accessibility_id('Header')
        except:
            cls.header = cls.session.find_element_by_accessibility_id('ContentPresenter')

        assert cls.session is not None
        assert cls.header is not None

        # init touch screen object
        # cls.touchScreen = webdriver.Remote()

        if (cls.header.text).lower() != 'standard':
            try:
                # Current version of Calculator application
                cls.session.find_element_by_accessibility_id('TogglePaneButton').click()
            except:
                # Previous version of Calculator application
                cls.session.find_element_by_accessibility_id('NavButton').click()

            import time
            time.sleep(1)
            splitViewPane = cls.session.find_element_by_class_name('SplitViewPane')
            splitViewPane.find_element_by_name('Standard Calculator').click()
            time.sleep(1)
            assert cls.header.text.lower() == 'standard'

    def teardown_class(cls):
        logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        cls.header = None
        cls.touchScreen = None
        if cls.session != None:
            cls.session.quit()
            cls.session = None

    @classmethod
    def getStaleElement(cls):
        assert cls.session is not None
        cls.session.find_element_by_accessibility_id('ClearMemoryButton').click()
        cls.session.find_element_by_accessibility_id('clearButton').click()
        cls.session.find_element_by_accessibility_id('memButton').click()

        try:
            # Locate the Memory pivot item tab that is displayed in expanded mode
            cls.session.find_element_by_accessibility_id('MemoryLabel').click()
        except:
            # Open the memory flyout when the calculator is in compact mode
            cls.session.find_element_by_accessibility_id('MemoryButton').click()
        import time
        time.sleep(1)
        staleElement = cls.session.find_element_by_accessibility_id('MemoryListView').find_element_by_name('0')
        cls.header.click()
        time.sleep(2)
        return staleElement

class TestCalculatorBase_UT(TestCalculatorBase):



    def test_zero(cls):
        assert cls.session is not None

    def test_one(self):
        assert self.session is not None
        # calc = TestCalculatorBase()  # dont need this, 

        elem = self.getStaleElement()
        # assert elem is not None
