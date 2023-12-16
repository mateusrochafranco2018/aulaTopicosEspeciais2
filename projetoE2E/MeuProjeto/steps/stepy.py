from behave import given, when, then
import time

@given('o usuario abrir o aplicativo')
def step_open_app(context):
    context.login_page.open_app()
@when('usuario tentar realizar login pelo email')
def step_click_sign_email_button(context):
    context.login_page.click_sign_email_button()    
    context.login_page.click_email_button()

@when('o usuario clicar no botao Email')
def step_click_email_button(context):    
    pass
@then('validar se foi apresentado a mensagem de erro "{expected_text}"')
def step_verify_error_message(context, expected_text):
    assert context.login_page.verify_error_message(expected_text), f"Mensagem de erro não corresponde a '{expected_text}'"
    assert context.login_page.is_error_message_visible(), "Mensagem de erro não está visível."
    