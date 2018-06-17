from Ligacoes import Ligacoes;

class Automato(object):
    Identificador = '';
    Ligacoes = [];

    def __init__(self, ident):
        self.Identificador = ident;

    def AddLigacao(self, Origem, Destino):
        self.Ligacoes.append(Ligacoes(Origem, Destino));
        print('Adicionado ligações',Origem,Destino);        
