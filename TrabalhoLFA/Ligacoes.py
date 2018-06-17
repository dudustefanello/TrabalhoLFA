class Ligacoes(object):
    Origem = "";
    Destino = "";


    Ativo = False;
    Visitado = False;
    Morto = False;
    Inalcancavel = False;
    EhFinal = False;

    def __init__(self, Origem, Destino):
        self.Origem = Origem;
        self.Destino = Destino;