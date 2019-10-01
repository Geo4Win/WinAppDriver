import pytest
import time
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from .appsessionbase.utility import Utility
from .appsessionbase.commontestsettings import CommonTestSettings, ErrorStrings
from .appsessionbase.test_edgebase import TestEdgeBase

import  logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class TestWindow():
    session :webdriver.Remote = None

    def teardown_method(self):
        if self.session:
            self.session.quit()
            self.session = None
    def test_closeWindow(self):
        self.session = Utility.createNewSession(CommonTestSettings.AlarmClockAppId)
        assert self.session is not None

        # close the application window without deleting the session
        self.session.close()
        assert self.session.session_id is not None
        time.sleep(5)
        assert self.session is not None

        #delete the session
        self.session.quit()
        self.session = None

    def test_CloseWindowError_NoSuchWindow(self):
        pass
        # attempt to close the previous closed application window
        #with pytest.raises(NoSuchWindowException, message = ErrorStrings.NoSuchWindow):
        #Utility.getOrphanedSession().close()


    def test_GetWindowHandle(self):
        self.session = Utility.createNewSession(CommonTestSettings.CalculatorAppId)
        assert self.session is not None
        windowHandle = self.session.current_window_handle
        assert windowHandle is not None

    def test_GetWindowHandleError_NoSuchWindow(self):
        pass

    def test_GetWindowHandles_ClassicApp(self):
        self.session = Utility.createNewSession(CommonTestSettings.NotepadAppId)
        assert self.session is not None
        handles = self.session.window_handles
        assert handles is not None
        assert len(handles) > 0

    def test_GetWindowHandles_Desktop(self):
        self.session = Utility.createNewSession(CommonTestSettings.DesktopAppId)
        assert self.session is not None
        handles = self.session.window_handles
        assert  handles is not None
        assert len(handles) == 0


    def test_GetWindowHandles_ModernApp(self):
        self.session = Utility.createNewSession(CommonTestSettings.EdgeAppId, "-private")
        assert self.session is not None

        windowHandlesBefore = self.session.window_handles
        assert windowHandlesBefore is not None
        assert len(windowHandlesBefore) > 0

        # preserve previously opened Edge window(s) and only maniplulate newly opened windows
        previouslyOpenedEdgeWindows = list(windowHandlesBefore)
        previouslyOpenedEdgeWindows.remove(self.session.current_window_handle)

        # set focus on itself
        self.session.switch_to.window(self.session.current_window_handle)

        # open a new window in private mode
        keys = Keys.CONTROL + Keys.SHIFT + 'p' + Keys.SHIFT + Keys.CONTROL
        element :webdriver.Remote = self.session.switch_to.active_element
        element.send_keys(keys)
        time.sleep(3)
        windowHandlesAfter = self.session.window_handles
        assert windowHandlesAfter is not None
        assert len(windowHandlesBefore) + 1 == len(windowHandlesAfter)

        # preserve previously opened Edge windows by only closing newly opened window
        newlyOpenedEdgeWindows = list(windowHandlesAfter)
        for previouslyOpenedWindow in previouslyOpenedEdgeWindows:
            newlyOpenedEdgeWindows.remove(previouslyOpenedWindow)

        for windowHandle in newlyOpenedEdgeWindows:
            self.session.switch_to.window(windowHandle)
            TestEdgeBase.closeEdge(self.session)





    def test_SwitchWindows(self):
        self.session = Utility.createNewSession(CommonTestSettings.EdgeAppId, CommonTestSettings.EdgeAboutBlankURL)
        assert self.session is not None

        # preserve previously opened Edge window(s) and only manipulate newly opened window
        previouslyOpenedEdgeWindows = list(self.session.window_handles)
        previouslyOpenedEdgeWindows.remove(self.session.current_window_handle)

        # set focus on itself
        self.session.switch_to.window(self.session.current_window_handle)

        # open a new window in private mode
        keys = Keys.CONTROL + Keys.SHIFT + 'p' + Keys.SHIFT + Keys.CONTROL
        element: webdriver.Remote = self.session.switch_to.active_element
        element.send_keys(keys)
        #Keys.SHIFT + Keys.CONTROL
        time.sleep(3)
        multipleWindowHandles = self.session.window_handles
        assert len(multipleWindowHandles) > 1

        # preserve previously opened Edge windows by only operating on newly
        newlyOpenedEdgeWindows = list(multipleWindowHandles)
        for presiouslyOpenedEdgeWindow in previouslyOpenedEdgeWindows:
            newlyOpenedEdgeWindows.remove(presiouslyOpenedEdgeWindow)

        previousWindowHandle = ''
        for windowHandle in newlyOpenedEdgeWindows:
            self.session.switch_to.window(windowHandle)
            assert self.session.current_window_handle == windowHandle
            assert self.session.current_window_handle != previousWindowHandle

            previousWindowHandle = windowHandle
            TestEdgeBase.closeEdge(self.session)









    def test_SwitchWindowsError_EmptyValue(self):
        pass

    def test_SwitchWindowsError_ForeignWindowHandle(self):
        pass

    def test_SwitchWindowsError_InvalidValue(self):
        pass

    def test_SwitchWindowsError_NonTopLevelWindowHandle(self):
        pass

    def test_SwitchWindowsError_NoSuchWindow(self):
        pass

