# BDD = Exemplificar com testes casos de uso (features) do sistema/classes e assim colaborar com um time utilizando uma linguagem humana. 
# Pode ser lido por Stakeholder/PO/Scrum Master 

Feature: Calcular a média de 2 números
  Scenario: Realizar uma soma e dividir o resultado por 2
    Given eu tenho dois números inteiros: 10 e 32
    When eu somo os dois números inteiros
    And eu divido a soma por 2
    Then o resultado deve ser 21