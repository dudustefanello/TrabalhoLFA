from EspsilonTransicao import EspsilonTransicao;
from Determinizacao import Determinizacao;
from Automatos import Automato;

automato = Automato();    # Incializa o automato com o arquivo de entrada
automato.carrega('liguagem.txt');                     # Carrega o automato a partir da 
automato.imprimir('\n\n######################## AUTOMATO LIDO: ########################\n'); # Imprimir automato final

livreEpsilon = EspsilonTransicao(automato)
livreEpsilon.eliminarEpsilonTransicoes();     # Busca os épsilon transições e trata as mesmas;
livreEpsilon.imprimir(); # Imprimir automato final

determinizado = Determinizacao(automato)
determinizado.determinizar();
determinizado.imprimir(); # Imprimir automato final

automato.removerInalcancaveis();
automato.imprimir('\n\n###################### SEM INALCANÇAVEIS: ######################\n'); # Imprimir automato final

automato.removerMortos();
automato.imprimir('\n\n########################## SEM MORTOS: #########################\n'); # Imprimir automato final

