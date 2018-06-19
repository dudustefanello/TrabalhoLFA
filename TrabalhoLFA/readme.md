# Trabalho Final - Linguagens Formais e Automatos

## Objetivo

Implementar um algoritmo computacional que gere um Automato Finito Determinístico Mínimo, livre de épsilon transições e sem a aplicação de classes de equivalência entre estados.

### Parâmetros de Projeto

* *Linguagem utilizada:* Python;
* *Notação Utilizada:* BFN;

# Clases

## Automatos

A Classe dos Automatos é a classe que faz a carga do automato do arquivo de texto para a estrutura inicial.

## Estados

A Classe dos Estados é a classe que contém a estrutura de uma estado, com suas flags e seu vetor de produções.

## Producoes

A Classe das Produções é a classe que contém a estrutura de uma produção, com suas flags, token e estado destino.

## Deterministico

A Classe Determinístico contém as regras que farão a determinização do automato após a eliminação de epsilon transição.