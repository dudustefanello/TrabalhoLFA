from Producoes import Producoes;

class Estados(object):
    Identificador = 0;
    Producoes = [];
    Origem = [];

    Ativo = True;
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
