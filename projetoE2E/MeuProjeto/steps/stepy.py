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

@when('o usuário clicar no botão jogar')
def step_clicar_botão_play_as_guest(context):
    context.login_page.click_play_as_guest_button()


@then('o aplicativo deve redirecionar para tela com algumas opções para iniciar a partida')
def step_botao_sing_in_visible(context):
    assert context.paginal_inicial_Sem_Realizar_login.botao_sing_in_visible(), "Botão não está visivel"

@when('o usuário clicar no texto Resolva Problemas')
def step_impl(context):
   context.login_page.click_play_as_guest_button()
   context.login_page.click_puzzles()



@then('o aplicativo deve redirecionar para tela com o primeiro problema')
def step_impl(context):
    assert context.login_page.tela_puzzle(), "Tela Incorreta"


@when('o usuário clicar no texto more')
def step_impl(context):
    context.login_page.click_play_as_guest_button()
    context.login_page.clicar_botao_more()


@then(u'o aplicativo deve redirecionar para More')
def step_impl(context):
    assert context.login_page.tela_more(), "Tela Incorreta"