import pytest
from logging import log
from appium import webdriver


# webdriver.Remote()
from .commontestsettings import CommonTestSettings, ErrorStrings
from .webdriverapiextensions import findCalculatorTitleByAccessibilityId, dismissAlarmDialogIfThere



import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class Utility():
    orphanedSession = None
    orphanedElement = None
    orphanedWindowHandle = None

    @classmethod
    def createNewSession(cls, appId, argument = None) -> webdriver.Remote:
        appCapabilities  = {'app' : appId}
        if argument:
            appCapabilities ['appArguments' ] = argument
        return webdriver.Remote(
            command_executor=CommonTestSettings.WindowsApplicationDriverUrl,
            desired_capabilities=appCapabilities)

    @classmethod
    def currentWindowIsAlive(cls, remoteSession : webdriver.Remote = None) -> bool:
        windowIsLive = False
        if remoteSession:
            try:
                window_handle = remoteSession.current_window_handle
                logger.info('window handle = {}'.format( window_handle))

                windowIsLive = window_handle !='0' and len(window_handle)>0
                windowIsAlive = True #??????????????
            except Exception as e:
                pass
                #print(e)
                #raise e
        return windowIsLive

    @classmethod
    def getOrphanedElement(cls):
        if cls.orphanedSession is None or cls.orphanedElement is None:
            cls.initializeOrphanedSession()
        return cls.orphanedElement

    @classmethod
    def getOrphanedSession(cls):
        #// Re-initialize orphaned session and element if they are compromised
        if cls.orphanedSession is None or cls.orphanedElement is None:
            cls.initializeOrphanedSession()
        return cls.orphanedSession

    @classmethod
    def getOrphanedWindowHandle(cls):
        if cls.orphanedSession is None or cls.orphanedElement is None or not cls.orphanedElement:
            cls.initializeOrphanedSession()
        return cls.orphanedWindowHandle

    @classmethod
    def cleanupOrphanedSession(cls):
        cls.orphanedWindowHandle = None
        cls.orphanedElement = None
        # clean up after the session if exists
        if(cls.orphanedSession is not None):
            cls.orphanedSession.quit()
            cls.orphanedSession = None

    @classmethod
    def initializeOrphanedSession(cls):
        #Create new calculator session and close the window to get an orphaned element
        cls.cleanupOrphanedSession()
        cls.orphanedSession = cls.createNewSession(CommonTestSettings.CalculatorAppId)
        cls.orphanedElement = findCalculatorTitleByAccessibilityId(cls.orphanedSession)
        cls.orphanedWindowHandle = cls.orphanedSession.current_window_handle
        cls.orphanedSession.close()
