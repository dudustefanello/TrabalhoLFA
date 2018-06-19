# Trabalho Final - Linguagens Formais e Automatos

## Objetivo

Implementar um algoritmo computacional que gere um Automato Finito Determin�stico M�nimo, livre de �psilon transi��es e sem a aplica��o de classes de equival�ncia entre estados.

### Par�metros de Projeto

* *Linguagem utilizada:* Python;
* *Nota��o Utilizada:* BFN;

# Clases

## Automatos

A Classe dos Automatos � a classe que faz a carga do automato do arquivo de texto para a estrutura inicial.

## Estados

A Classe dos Estados � a classe que cont�m a estrutura de uma estado, com suas flags e seu vetor de produ��es.

## Producoes

A Classe das Produ��es � a classe que cont�m a estrutura de uma produ��o, com suas flags, token e estado destino.

## Deterministico

A Classe Determin�stico cont�m as regras que far�o a determiniza��o do automato ap�s a elimina��o de epsilon transi��o.