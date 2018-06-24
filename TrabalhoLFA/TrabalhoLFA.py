from Automatos import Automato;

Indeterministico = Automato('liguagem.txt');    #Incializa o automato com o arquivo de entrada

Indeterministico.carrega();                 # Carrega o automato a partir da string
Indeterministico.buscarIndeterminismo();    # Busca indeterminismos para determinizar
Indeterministico.imprimir();                # Imprimir automato final
                




