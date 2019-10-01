import  pytest
from .commontestsettings import CommonTestSettings, ErrorStrings
from .utility import Utility
class TestUtility():

    def test_createNewSession(self):
        appId = CommonTestSettings.CalculatorAppId
        session = Utility.createNewSession(appId)
        session.quit()

    def test_currentWindowIsAlive(self):
        appId = CommonTestSettings.CalculatorAppId
        session = Utility.createNewSession(appId)
        isLive = Utility.currentWindowIsAlive( session)
        assert isLive == True
        session.quit()

    def test_cleanupOrphanedSession(self):
        Utility.cleanupOrphanedSession()
        assert Utility.orphanedSession is None
        assert Utility.orphanedWindowHandle is None
        assert Utility.orphanedElement is None

    def test_initializeOrphanedSession(self):
        Utility.initializeOrphanedSession()
        assert Utility.orphanedSession is not None
        assert Utility.orphanedWindowHandle is not None
        assert Utility.orphanedElement is not None
    def test_getOrphanedElement(self):
        elem = Utility.getOrphanedElement()
        assert elem is not None

    def test_getOrphanedWindowHandle(self):
        handle = Utility.getOrphanedWindowHandle()
        assert handle is not None

    def test_getOrphanedSession(self):
        session = Utility.getOrphanedSession()
        assert session is not None
