from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

def before_all(context):
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": "com.chess",
        "appActivity": ".splash.SplashActivity",
        "ensureWebviewsHavePages": True,
        "nativeWebScreenshot": True,
        "newCommandTimeout": 3600,
        "connectHardwareKeyboard": True
    }

    options = UiAutomator2Options()
    options.load_capabilities(caps)
    context.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

def after_all(context):
    context.driver.quit()