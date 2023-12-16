from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('o usuario abrir o aplicativo')
def passo_abrir_aplicativo(context):
    # Lógica para abrir o aplicativo, se necessário
    pass

@when('usuario tentar realizar login pelo email')
def passo_tentar_login_email(context):
    context.driver.find_element(by=AppiumBy.ID, value="com.chess:id/text").click()  # Ajuste aqui conforme necessário

@when('o usuario clicar no botao Email')
def passo_clicar_botao_email(context):
    wait = WebDriverWait(context.driver, 10)
    email_button = (By.ID, "com.chess:id/continueWithEmailBtn")
    # Aguarda até que o botão de email seja visível
    try:
        elemento_email = wait.until(EC.element_to_be_clickable(email_button))
        # Clica no botão
        elemento_email.click()
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")

@then('validar se foi apresentado a mensagem de erro')
def passo_verificar_texto(context):
    # Aguarda até que o elemento com o ID "com.chess:id/textinput_error" esteja visível
    wait = WebDriverWait(context.driver, 10)  # Aguarda até 10 segundos
    try:
        elemento = wait.until(EC.visibility_of_element_located((By.ID, "com.chess:id/textinput_error")))
        texto_obtido = elemento.text
        texto_esperado = "This value is not a valid email address"
        assert texto_obtido == texto_esperado, f"O texto obtido '{texto_obtido}' não é igual ao texto esperado '{texto_esperado}'"
    except Exception as e:
        print(f"Erro ao validar a mensagem de erro: {e}")
