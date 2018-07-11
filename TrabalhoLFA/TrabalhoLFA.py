from EspsilonTransicao import EspsilonTransicao   # Importa a implementação da eliminação de épsilon transições
from Determinizacao import Determinizacao       # Importa a implementação da determinização
from Inalcancaveis import Inalcancaveis         # Importa a implementação da remoção de inalcançáveis
from Automatos import Automato                  # Importa as implementações gerais do automato
from Mortos import Mortos                       # Importa a implementação de remoção de mortos

automato = Automato()                           # Instancia a classe Automato
automato.carrega('liguagem.txt')                # Carrega o automato a partir do arquivo de texto
automato.imprimir('\n\n# AUTOMATO LIDO:\n')     # Imprime automato lido

livreEpsilon = EspsilonTransicao(automato)       # Instancia o objeto para remover epsilons transicões
livreEpsilon.eliminarEpsilonTransicoes()        # Busca as épsilon transições e trata as mesmas
livreEpsilon.imprimir()                         # Imprimir automato livre de épsilon transições

determinizado = Determinizacao(automato)        # Instancia o objeto para determinização
determinizado.determinizar()                    # Faz a determinização do autômato
determinizado.imprimir()                        # Imprimir automato determinizado

#automato.removerInalcancaveis();
#automato.imprimir('\n\n###################### SEM INALCANÇAVEIS: ######################\n'); # Imprimir automato final

#automato.removerMortos();
#automato.imprimir('\n\n########################## SEM MORTOS: #########################\n'); # Imprimir automato final

semInalcancaveis = Inalcancaveis(automato)      # Instancia o objeto para remover estados inalcançáveis
semInalcancaveis.removerInalcancaveis()         # Remove os estados inalcançáveis
semInalcancaveis.imprimir()                     # Imprimir automato final

semInalcancaveis = Mortos(semInalcancaveis)             # Instancia o objeto para remover estados mortos
semInalcancaveis.removerMortos()                # Remove os estados mortos
semInalcancaveis.imprimir()                     # Imprime automato minimizado


