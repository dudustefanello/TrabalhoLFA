from Inuteis import Inuteis
from Producao import Producao

class Inalcancaveis(Inuteis):
    
    def __init__(self, automato):
        super(Inalcancaveis, self).__init__(automato)


    def imprimir(self):
        return super().imprimir('\n\n# SEM INALCANCAVEIS:\n')

          
    def removerInalcancaveis(self):
        estados = self.gerarEstadosParaMinimizacao()
        self.visitaNovaProducaoInalcancavel(estados, 0)


    def visitaNovaProducaoInalcancavel(self, estados, transicao):
         if transicao in estados:
             if transicao in self.Finais:
                 self.adicionaAutomatoMinimizado(transicao,-1,-1)

             for producao in estados[transicao]:
            
                if not estados[transicao][producao].temProducao():        #caso não tenha uma produção válida
                    continue
            
                if estados[transicao][producao].visitado:
                    return
        
                estados[transicao][producao].visitado = True
                self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao)
                self.visitaNovaProducaoInalcancavel(estados, estados[transicao][producao].producao)  