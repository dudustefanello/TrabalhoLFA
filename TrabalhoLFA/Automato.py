from Producoes import Producoes;

class Automato(object):
    Identificador = 0;
    Producoes = [];

    Ativo = True;
    Visitado = False;
    Morto = False;
    Inalcancavel = False;
    Final = False;

    def __init__(self, ident):
        self.Identificador = ident;
        self.Producoes = [];
        print('Adicionado estado', ident);        

    def AddLigacao(self, Token, Destino):
        self.Producoes.append(Producoes(Token, Destino));
        print('Adicionado produção', str(Token) +'<' + str(Destino) + '>');        
