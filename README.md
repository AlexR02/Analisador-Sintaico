# Analisador Sintático em Python para C

## Compilação

Para compilar o programa é necessário utilizar o python3 e basta utilizar o seguinte comando no terminal:

``python3 analiseLexica.py`` 

O retorno da execução será um print contendo todos os tokens encontrados e sua devida descrição.

## Sobre o Analisador
O analisador desenvolvido tem como o intuito separar em tokens um código simples escrito em C com algumas contas matemáticas. Após identificados os tokens eles são inseridos em um dicionário, como o dicionário é baseado em chave e valor ,chaves repetidas não são inseridas novamente, o que não é necessário e ainda economiza memória. Essa análise é uma melhora da Léxica e também realiza verificações como balanceamento de parênteses e chaves por exemplo, a ideia era incluir a estruturação de declarações de variáveis e passagem de parâmetros em funções também, mas foram encontrados problemas nessas implementações e elas serão feitas assim que possível.
