from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from pages.login_page import LoginPage
from pages.paginal_inicial_Sem_Realizar_login import PaginaInicialSemRealizarLogin

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

    # Inicialização da página de login
    context.login_page = LoginPage(context.driver)
    # Inicialização da página de login
    context.paginal_inicial_Sem_Realizar_login = PaginaInicialSemRealizarLogin(context.driver)

def after_all(context):
    context.driver.quit()
