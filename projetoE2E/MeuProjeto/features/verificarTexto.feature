Feature: Verificar Texto

  Scenario: Verificar texto exibido no aplicativo
    Given o usuario abrir o aplicativo
    When usuario tentar realizar login pelo email
    And o usuario clicar no botao Email
    Then validar se foi apresentado a mensagem de erro