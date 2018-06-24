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




class Automato(object):

Estados = dict();

# -- Leitura de arquivos:
def __init__(self, arquivo):

    self.Estados = {};  # Inicializa o dictionary da classe

    arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
    texto = arquivo.read();         # L� o arquivo de entrada
    self.carrega(texto);            # Carrega o automato a partir do arquivo de texto


# -- Inser��o de Tokens da Linguagem
def carregaTokens(self, word, New):
    if word == '\n':
        New = True; # Flag de nova palavra
    else:
        if New:
            if word in self.Estados[0]:                                # Se o Token j� existe no estado
                self.Estados[0][word].append(len(self.Estados));       # Ent�o adiciona referenciando o token
            else:
                self.Estados[0].update({word: [len(self.Estados)]});   # Sen�o carrega no estado inicial, criando novo token

            self.Estados.update({len(self.Estados):{}});            # Cria o pr�ximo estado para continua��o
            New = False;
        else:
            self.Estados[len(self.Estados) - 1].update({word: [len(self.Estados)]});   # Insere no �ltimo estado criado
            self.Estados.update({len(self.Estados):{}});                            # Cria o pr�ximo estado para continua��o


# -- Inser��o das regras da Gram�tica Regular
def carregaGramatica(self, word):
    pass
        

# -- Inser��o no automato:
def carrega(self, texto):

    New = True;

    self.Estados.update({len(self.Estados):{}});

    for a in texto:
        a = a.lower();  # Utiliza letra em minusculo
           
        if a == '\n' and New:   # Identifica quebra de linha
            self.carregaGramatica(a);
        else:
            self.carregaTokens(a, New);
                


                

