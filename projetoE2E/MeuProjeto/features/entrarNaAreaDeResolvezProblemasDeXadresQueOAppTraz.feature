Feature: Entrar na área de resolver problemas de xadrez que o app traz
  Scenario: Entrar na área de resolver problemas de xadrez que o app traz
    Given o usuario abrir o aplicativo
    When o usuário clicar no texto Resolva Problemas
    Then o aplicativo deve redirecionar para tela com o primeiro problema
