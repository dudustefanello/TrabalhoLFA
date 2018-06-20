# Trabalho Final - Linguagens Formais e Automatos

## Objetivo

Implementar um algoritmo computacional que gere um Automato Finito Determin�stico M�nimo, livre de �psilon transi��es e sem a aplica��o de classes de equival�ncia entre estados.

### Par�metros de Projeto

* *Linguagem utilizada:* Python;
* *Nota��o Utilizada:* BFN;

# Estrutura do Automato Indetermin�stico

A Classe dos Automatos � a classe que faz a carga do automato do arquivo de texto para a estrutura inicial.

A estrutura consiste de:

* Dictionary de Estados:
	* Cada Estado � um Dictionary de Produ��es:
		* Cada Token � um �ndice para uma lista de estados-destino.