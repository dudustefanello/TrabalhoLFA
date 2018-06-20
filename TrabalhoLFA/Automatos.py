from Producoes import Producoes;
from Estados import Estados;

class Automato(object):

    Estados = [];
    
    def __init__(self, arquivo):
        # -- Leitura de arquivos:
        
        self.Automato = [];             # Inicializa o vetor da classe
        arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
        texto = arquivo.read();         # Lê o arquivo de entrada
        self.carrega(texto);            # Carrega o automato a partir do arquivo de texto


    def carrega(self, texto):
        # -- Inserção no automato:

        New = True;

        self.Estados.append(Estados(0));  # Insere o estado final

        for a in texto:
            a = a.lower();   # Colocar letra em minusculo
           
            if a == '\n':                       # Identificar quebras de linha
                New = True;                     # Flag de nova palavra
                self.Estados[-1].Final = True;  # Marca o Estado como Final
            else:
                if New:
                    self.Estados[0].AddLigacao(a, len(self.Estados)); # Carrega no estado inicial
                    self.Estados.append(Estados(len(self.Estados)));  # Cria o estado para continuação

                    New = False;
                else:
                    self.Estados[-1].AddLigacao(a, len(self.Estados)); # Insere no último estado criado
                    self.Estados.append(Estados(len(self.Estados)));   # Cria o estado para continuação 
    
                    
    def imprimeTela(self):
        # -- Impressão do Automato

        for i in self.Estados: # Loop no automato
            if i.Final:
                print('*', end=''); # Marca asterisco para estados que são finais
            else:
                print(' ', end=''); # Coloca espaço para compesar asterisco
            
            print('<' + str(i.Identificador) + '> ::= | ', end=''); # Insere o identificador da regra
            
            for j in i.Producoes:                                       # Loop nas produções do estado selecionado
                print(j.Token + '<' + str(j.Destino) + '> | ', end=''); # Insere as produções
            
            print('');  # Insere quebra de linha ao final de cada estado            


                

