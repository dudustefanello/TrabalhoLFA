from Automatos import Automato

class Determinizacao(Automato):
    
    def __init__(self, automato):
        super(Determinizacao, self).__init__()

        self.Estados = automato.Estados
        self.Alfabeto = automato.Alfabeto
        self.Finais = automato.Finais
        

    def imprimir(self):
        return super().imprimir('\n\n# DETERMINIZADO:\n')


    def determinizar(self):
        self.buscarIndeterminismo()  
        
    def adicionaEstadoFinal(self, producoes, novaProducao):
        for producao in producoes:
            if producao in self.Finais:
                self.Finais.add(novaProducao)

                
    def substituiNovaProducao(self):
        if len(self.NovasProducoes) > 0:            
            for transicoes in self.Estados:
                for letra in sorted(self.Alfabeto): 
                    if len(self.Estados[transicoes][letra]) > 1:
                        producaoAgrupadaTemp = self.geraProducaoAgrupada(self.Estados[transicoes][letra])
                        if producaoAgrupadaTemp in self.NovasProducoes:
                            self.Estados[transicoes][letra] = [self.NovasProducoes[producaoAgrupadaTemp][0]]


    # -- Percorre o autômato identificando e tratando seus indeterminismos
    def buscarIndeterminismo(self):
        qtdEstados = len(self.Estados)                                         # Marca a quantidade inicial de estados do autômato
        i = 0                                                                  # Zera a variável de índice
        while i < qtdEstados:                                                   # Faz um loop pelos estados
            for j in sorted(self.Alfabeto):                                     # Itera um laço pelo conjunto de símbolos do alfabeto
                if i in self.Estados and len(self.Estados[i][j]) > 1:           # Se houver uma transição estiver indeterminada:
                    self.determinizarProducao(self.Estados[i][j])                                     # Determiniza o estado

                    qtdEstados = len(self.Estados)                             # Atualiza a quantidade de estados
            i += 1                                                             # Incrmenta o índice.
            
            if i == qtdEstados:
                for novoEstado in list(self.NovasProducoes):
                    if self.NovasProducoes[novoEstado][0] not in self.Estados:
                        self.determinizarProducao(self.NovasProducoes[novoEstado][1]) 
                        qtdEstados = len(self.Estados) 


    # -- Determiniza um estado do automato
    def determinizarProducao(self, producoes):        
        estadoTemporario = dict()                                                  # Cria um estado temporário
        #novoEstado = len(self.Estados)                                             # Dá nome/número ao estado que será criado
        #producoes = transicoes
        producaoAgrupada = self.geraProducaoAgrupada(producoes) 

        #if producaoAgrupada in self.NovasProducoes:
        #    self.Estados[transicao][producao] = [self.NovasProducoes[producaoAgrupada][0]]

        if ((producaoAgrupada not in self.NovasProducoes) or (self.NovasProducoes[producaoAgrupada][0] not in self.Estados)):            
            if (len(producoes) > 1) and (not self.existeProducaoAgrupada(producoes)):
                novoEstado = self.pegarNovoEstadoDetrminizacao()
                self.NovasProducoes.update({self.geraProducaoAgrupada(producoes): [novoEstado,producoes]})
            for i in producoes:                                                         # Faz um loop nas produções que que contém a indeterminação
                for j in sorted(self.Alfabeto):                                         # Faz um loop no conjunto de símbolos do alfabeto
                    if j in estadoTemporario:                                           # Se o o símbolo j já estiver no estado temporário:                        
                        lista = list(set(estadoTemporario[j] + self.pegarProducaoOriginal(self.Estados[i][j])))    # Adiciona a lista de transições de j
                        estadoTemporario[j] = lista                                    # ao estado
                    
                        if (len(lista) > 1) and (not self.existeProducaoAgrupada(lista)):
                            novoEstado = self.pegarNovoEstadoDetrminizacao()
                            self.NovasProducoes.update({self.geraProducaoAgrupada(lista): [novoEstado,lista]})

                    else:
                        producaoAtual = list(set(self.Estados[i][j]))
                        
                        if len(producaoAtual) > 1:
                            producaoAgrupadaTemp = self.geraProducaoAgrupada(producaoAtual)
                            if self.existeProducaoAgrupada(producaoAgrupadaTemp):
                                estadoTemporario.update({j: list(set(self.NovasProducoes[producaoAgrupada][1]))})
                        
                        elif (len(producaoAtual) > 0) and (self.existeNovoEstado(producaoAtual[0])):
                            for prod in self.NovasProducoes:
                                if self.NovasProducoes[prod][0] == producaoAtual[0]:
                                    estadoTemporario.update({j: list(set(self.NovasProducoes[prod][1]))})
                        else:
                            estadoTemporario.update({j: producaoAtual})
        
            super().setAlfabetoEstado(estadoTemporario)                                   # Relaciona o estado temporário com os símbolos do alfabeto                    
            self.Estados.update({self.NovasProducoes[producaoAgrupada][0]: estadoTemporario})                        # Adiciona o estado temporário ao dicionário de estados da classe
            self.adicionaEstadoFinal(producoes, self.NovasProducoes[producaoAgrupada][0])
            self.substituiNovaProducao()

        return


    def geraProducaoAgrupada(self, lista):
        estado = ''
        for item in lista:
            if estado == '':
                estado += str(item)
            else:
                estado += ',' + str(item)

        return estado


    def existeProducaoAgrupada(self, lista):
        retorno = False

        if len(lista) > 1:
            producaoAgrupadaTemp = self.geraProducaoAgrupada(lista)
            return (producaoAgrupadaTemp in self.NovasProducoes)
        else:
            for i in self.NovasProducoes:
                if lista[0] in self.NovasProducoes[i][1]:
                    return True
        return retorno


    def pegarNovoEstadoDetrminizacao(self):
        novasProducoes = []
        for producao in self.NovasProducoes:
            novasProducoes.append(self.NovasProducoes[producao][0])

        return len(set(list(self.Estados) + novasProducoes))
   
    
    def pegarProducaoOriginal(self, producaoOrig):
        retorno = list(set(producaoOrig))
        for producao in self.NovasProducoes:
            for prod in producaoOrig:
                if self.NovasProducoes[producao][0] == prod:
                    retorno = list(set(self.NovasProducoes[producao][1]))

        return retorno
    

    def existeNovoEstado(self, producao):
        if len(self.NovasProducoes) > 0:
            for producaoAgrupada in self.NovasProducoes:
                if self.NovasProducoes[producaoAgrupada][0] == producao:
                    return True

        return False
