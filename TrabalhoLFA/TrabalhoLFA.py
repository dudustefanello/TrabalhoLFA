from EspsilonTransicao import EspsilonTransicao;
from Determinizacao import Determinizacao;
from Inalcancaveis import Inalcancaveis;
from Automatos import Automato;
from Mortos import Mortos;

automato = Automato();    # Incializa o automato com o arquivo de entrada
automato.carrega('liguagem.txt');                     # Carrega o automato a partir da 
automato.imprimir('\n\n# AUTOMATO LIDO:\n'); # Imprimir automato final

livreEpsilon = EspsilonTransicao(automato)
livreEpsilon.eliminarEpsilonTransicoes();     # Busca os épsilon transições e trata as mesmas;
livreEpsilon.imprimir(); # Imprimir automato final

determinizado = Determinizacao(automato)
determinizado.determinizar();
determinizado.imprimir(); # Imprimir automato final

semInalcancaveis = Inalcancaveis(automato)
semInalcancaveis.removerInalcancaveis();
semInalcancaveis.imprimir(); # Imprimir automato final

semInalcancaveis = Mortos(automato)
semInalcancaveis.removerMortos();
semInalcancaveis.imprimir(); # Imprimir automato final

