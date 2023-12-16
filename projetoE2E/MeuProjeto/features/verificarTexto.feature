Feature: Verificar Texto

  Scenario: Verificar texto exibido no aplicativo
    Given o usuario abrir o aplicativo
    When usuario tentar realizar login pelo email
    Then validar se foi apresentado a mensagem de erro "This value is not a valid email address."
