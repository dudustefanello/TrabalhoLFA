from Producoes import Producoes;
from Regras import Regras;

class Automatos(object):

    Automato = [];
    
    def __init__(self, arquivo):
        # -- Leitura de arquivos:
        self.Automato = [];
        arquivo = open(arquivo, 'r');
        texto = arquivo.read();
        self.carrega(texto);


    def carrega(self, texto):
        # -- Inserção no automato:

        New = True;

        self.Automato.append(Regras(0));

        for a in texto:
            a = a.lower();  # Colocar letra em minusculo
            if a == '\n':   # Identificar quebras de linha
                New = True; # Flag de nova palavra
            else:
                if New:
                    self.Automato[0].AddLigacao(a, len(self.Automato)); # Carrega no estado inicial
                    self.Automato.append(Regras(len(self.Automato)));   # Cria o estado para continuação
                    New = False;
                else:
                    self.Automato[-1].AddLigacao(a, len(self.Automato)); # Insere no último estado criado
                    self.Automato.append(Regras(len(self.Automato)));    # Cria o estado para continuação 
    
                    
    def imprimeTela(self):
        # -- Impressão do Automato
        for i in self.Automato:
            if len(i.Producoes) == 0:
                i.Final = True;
                print('*', end='');
            else:
                print(' ', end='');
            print('<' + str(i.Identificador) + '> ::= | ', end='');
            for j in i.Producoes:
                print(j.Token + '<' + str(j.Destino) + '> | ', end='');
            print('');

