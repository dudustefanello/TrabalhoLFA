from Automatos import Automato;

automato = Automato('liguagem.txt');    # Incializa o automato com o arquivo de entrada

automato.carrega();                     # Carrega o automato a partir da 
automato.imprimir('\n\n######################## AUTOMATO LIDO: ########################\n'); # Imprimir automato final

automato.buscarEpsilonTransicoes();     # Busca os épsilon transições e trata as mesmas;
automato.imprimir('\n\n################## LIVRE DE EPSILON TRANSIÇÕES: ################\n'); # Imprimir automato final

automato.buscarIndeterminismo();        # Busca indeterminismos para determinizar
automato.imprimir('\n\n######################## DETERMINIZADO: ########################\n'); # Imprimir automato final

automato.removerInalcancaveis();
automato.imprimir('\n\n###################### SEM INALCANÇAVEIS: ######################\n'); # Imprimir automato final

automato.removerMortos();
automato.imprimir('\n\n########################## SEM MORTOS: #########################\n'); # Imprimir automato final

