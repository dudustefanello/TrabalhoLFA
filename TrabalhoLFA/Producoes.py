class Producoes(object):
    Token = '';
    Destino = 0;

    Visitado = False;

    def __init__(self, token, destino):
        self.Token = token;
        self.Destino = destino;