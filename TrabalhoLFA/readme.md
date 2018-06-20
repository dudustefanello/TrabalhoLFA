# Trabalho Final - Linguagens Formais e Automatos

## Objetivo

Implementar um algoritmo computacional que gere um Automato Finito Determinístico Mínimo, livre de épsilon transições e sem a aplicação de classes de equivalência entre estados.

### Parâmetros de Projeto

* *Linguagem utilizada:* Python;
* *Notação Utilizada:* BFN;

# Estrutura do Automato Indeterminístico

A Classe dos Automatos é a classe que faz a carga do automato do arquivo de texto para a estrutura inicial.

A estrutura consiste de:

* Dictionary de Estados:
	* Cada Estado é um Dictionary de Produções:
		* Cada Token é um índice para uma lista de estados-destino.