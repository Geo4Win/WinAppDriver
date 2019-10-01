

class CommonTestSettings(object):
    WindowsApplicationDriverUrl = "http://127.0.0.1:4723"

    AlarmClockAppId = "Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"
    CalculatorAppId = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    DesktopAppId = "Root";
    EdgeAppId = "Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge"
    ExplorerAppId = r"C:\Windows\System32\explorer.exe"
    NotepadAppId = r"C:\Windows\System32\notepad.exe"

    EdgeAboutBlankURL = "about:blank"
    EdgeAboutFlagsURL = "about:flags"
    EdgeAboutTabsURL = "about:tabs"

    TestFileName = r"TestFile"
    TestFolderLocation = r"%TEMP%"



class ErrorStrings(object):
    ElementNotVisible = "An element command could not be completed because the element is not pointer- or keyboard interactable."
    NoSuchElement = "An element could not be located on the page using the given search parameters."
    NoSuchWindow = "Currently selected window has been closed"
    StaleElementReference = "An element command failed because the referenced element is no longer attached to the DOM."
    UnimplementedCommandLocator = "Unexpected error. Unimplemented Command: {0} locator strategy is not supported"
    UnimplementedCommandTimeoutType = "Unexpected error. Unimplemented Command: {0} timeout type is not supported"
    XPathLookupError = "Invalid XPath expression: {0} (XPathLookupError)"

    ActionsNoSuchElement = "specified in the Actions origin is unknown or does not exist"
    ActionsNullElement = "element is not an Object that represents a web element"
    ActionsStaleElementReference = "specified in the Actions origin is no longer valid"
    ActionsUnimplementedPointerType = "Currently only pen and touch pointer input source types are supported"
    ActionsUnimplementedMultiPen = "Currently only a single (non-concurrent) pen input is supported"

    ActionsArgumentButton = "\"button\" in a pointer action JSON payload is undefined or is not an Integer greater than or equal to 0"
    ActionsArgumentDuration = "\"duration\" in a pointer action JSON payload is not an Integer greater than or equal to 0"
    ActionsArgumentOrigin = "\"origin\" in a action JSON payload is not equal to \"viewport\" or \"pointer\" and element is not an Object that represents a web element"
    ActionsArgumentParameterHeight = "\"height\" attribute is not a floating point value greater or equal to 1"
    ActionsArgumentParameterWidth = "\"width\" attribute is not a floating point value greater or equal to 1"
    ActionsArgumentParameterMissingWidthOrHeight = "\"width\" and \"height\" attributes need to be specified together"
    ActionsArgumentParameterPressure = "\"pressure\" attribute is not a floating point value between 0 and 1"
    ActionsArgumentParameterTiltX = "\"tiltX\" attribute is not an integer value between -90 and 90"
    ActionsArgumentParameterTiltY = "\"tiltY\" attribute is not an integer value between -90 and 90"
    ActionsArgumentParameterTwist = "\"twist\" attribute is not an integer value between 0 and 359"

