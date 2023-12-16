Feature: Iniciar uma partida contra o computador sem realizar login
    Scenario: Iniciar uma partida contra o computador sem realizar login
        Given o usuario abrir o aplicativo
        When o usuário clicar no botão jogar 
        Then o aplicativo deve redirecionar para tela com algumas opções para iniciar a partida
