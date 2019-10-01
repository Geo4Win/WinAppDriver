
import pytest
from appium import webdriver
from .commontestsettings import CommonTestSettings
def findCalculatorTitleByAccessibilityId( session :webdriver.Remote )  :
    try:
        element = session.find_element_by_accessibility_id('AppName')
        print('found by AppName')
    except:
        element = session.find_element_by_accessibility_id('AppNameTitle')
        print('found by AppNameTitle')

    return element

def dismissAlarmDialogIfThere(session: webdriver.Remote):

    try:
        session.find_element_by_accessibility_id('SecondaryButton').click()
    except Exception as e:  # dismiss only if found
        pass
        #print(e)
        #raise(e)
