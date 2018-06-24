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




class Automato(object):

Estados = dict();

# -- Leitura de arquivos:
def __init__(self, arquivo):

    self.Estados = {};  # Inicializa o dictionary da classe

    arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
    texto = arquivo.read();         # Lê o arquivo de entrada
    self.carrega(texto);            # Carrega o automato a partir do arquivo de texto


# -- Inserção de Tokens da Linguagem
def carregaTokens(self, word, New):
    if word == '\n':
        New = True; # Flag de nova palavra
    else:
        if New:
            if word in self.Estados[0]:                                # Se o Token já existe no estado
                self.Estados[0][word].append(len(self.Estados));       # Então adiciona referenciando o token
            else:
                self.Estados[0].update({word: [len(self.Estados)]});   # Senão carrega no estado inicial, criando novo token

            self.Estados.update({len(self.Estados):{}});            # Cria o próximo estado para continuação
            New = False;
        else:
            self.Estados[len(self.Estados) - 1].update({word: [len(self.Estados)]});   # Insere no último estado criado
            self.Estados.update({len(self.Estados):{}});                            # Cria o próximo estado para continuação


# -- Inserção das regras da Gramática Regular
def carregaGramatica(self, word):
    pass
        

# -- Inserção no automato:
def carrega(self, texto):

    New = True;

    self.Estados.update({len(self.Estados):{}});

    for a in texto:
        a = a.lower();  # Utiliza letra em minusculo
           
        if a == '\n' and New:   # Identifica quebra de linha
            self.carregaGramatica(a);
        else:
            self.carregaTokens(a, New);
                


                

