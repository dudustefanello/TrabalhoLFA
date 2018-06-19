from Producoes import Producoes;
from Estados import Estados;

class Automato(object):

    Automato = [];
    
    def __init__(self, arquivo):
        # -- Leitura de arquivos:
        
        self.Automato = [];             # Inicializa o vetor da classe
        arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
        texto = arquivo.read();         # Lê o arquivo de entrada
        self.carrega(texto);            # Carrega o automato a partir do arquivo de texto


    def carrega(self, texto):
        # -- Inserção no automato:

        New = True;

        self.Automato.append(Estados(0));  # Insere o estado final

        for a in texto:
            a = a.lower();   # Colocar letra em minusculo
           
            if a == '\n':                       # Identificar quebras de linha
                New = True;                     # Flag de nova palavra
                self.Automato[-1].Final = True; # Marca o Estado como Final
            else:
                if New:
                    self.Automato[0].AddLigacao(a, len(self.Automato)); # Carrega no estado inicial
                    self.Automato.append(Estados(len(self.Automato)));  # Cria o estado para continuação

                    New = False;
                else:
                    self.Automato[-1].AddLigacao(a, len(self.Automato)); # Insere no último estado criado
                    self.Automato.append(Estados(len(self.Automato)));   # Cria o estado para continuação 
    
                    
    def imprimeTela(self):
        # -- Impressão do Automato

        for i in self.Automato: # Loop no automato
            if i.Final:
                print('*', end=''); # Marca asterisco para estados que são finais
            else:
                print(' ', end=''); # Coloca espaço para compesar asterisco
            
                print('<' + str(i.Identificador) + '> ::= | ', end=''); # Insere o identificador da regra
            
            for j in i.Producoes:                                       # Loop nas produções do estado selecionado
                print(j.Token + '<' + str(j.Destino) + '> | ', end=''); # Insere as produções
            
            print('');  # Insere quebra de linha ao final de cada estado            


                

