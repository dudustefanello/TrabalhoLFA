from Automatos import Automato;

automato = Automato('liguagem.txt');    # Incializa o automato com o arquivo de entrada

automato.carrega();                     # Carrega o automato a partir da string
automato.buscarIndeterminismo();        # Busca indeterminismos para determinizar
automato.imprimir();                    # Imprimir automato final

              