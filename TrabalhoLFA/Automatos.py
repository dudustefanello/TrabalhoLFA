import re
from Producao import Producao;

FINAL = '$'
EPSILON = '#'

class Automato(object):

    # -- Declaração dos campos da classe
    Estados = dict();   # Estrutura que guarda todos os estados do autômato
    Alfabeto = set();   # Estrutura que contém todos os símbolos do alfabeto
    Finais = set();     # Estrutura que contém os estados que são finais
    Texto = str();      # Campo para guardar a string de entrada
    NovasProducoes = dict();
    TransicoesVisitadas = list();
    AutomatoMinimizado = dict();


    # -- Inicialização da classe:
    def __init__(self):
        self.Estados = dict();          # Inicializa o dictionary de estados com uma estrutura vazia
        self.Alfabeto = set();          # Inicializa o set do alfabeto com uma estrutura vazia
        self.Finais = set();            # Inicializa o set de estados finais com uma estrutura vazia
        self.NovasProducoes = dict();
        self.AutomatoMinimizado = dict();


    def leitura(self, arquivo):
        arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
        self.Texto = arquivo.read();    # Converte o arquivo para string


    # -- Inserção de Tokens da Linguagem
    def carregaToken(self, simbolo, new):
        self.Alfabeto.add(simbolo);                                                     # Adiciona o símbolo ao conjunto alfabeto

        if new:                                                                         # Se o símbolo for de um novo token:
            if simbolo in self.Estados[0]:                                              # Se o token já existir no estado:
                self.Estados[0][simbolo].append(len(self.Estados));                     # Adiciona na lista de estados destinos daquele token

            else:                                                                       # Se o token ainda não existir no estado:
                self.Estados[0].update({simbolo: [len(self.Estados)]});                 # Adiciona uma nova entrada para o token
            self.Estados.update({len(self.Estados): {}});                               # Cria um estado vazio para a próxima iteração

        if not new:                                                                     # Se o símbolo for de um token já existente:
            self.Estados[len(self.Estados) - 1].update({simbolo: [len(self.Estados)]}); # Insere no último estado criado
            self.Estados.update({len(self.Estados): {}});                               # Cria um estado vazio para a próxima iteração


    # -- Leitura das regras da Gramática Regular
    def carregaGramatica(self, textos):
        regras = dict();                                                        # Inicia a estrutura temporária para mapeamento das regras
        estados = dict();                                                       # Inicia a estrutura temporária para guardar os estados

        ignorar = [' ', ':'];                                                   # Lista de caracteres que devem ser ignorados na leitura        

        # - Insere uma nova regra no mapa de regras
        def novaRegra(self, texto):
            if texto == 'S':                                                        # Se o identificador do estado for S:
                estados.update({0: {}});                                            # Será adicionado no estado inicial                
                regras.update({'S': 0});                                            # E mapeado para o estado inicial

            else:                                                                   # Senão:
                numero = len(set(list(self.Estados) + list(estados)));                       # Será inserida uma regra no
                regras.update({texto: numero});                                     # último espaço do autômato                
                estados.update({regras[texto]: {}});                                # E mapeado para o número do último estado


        # - Insere uma nova transição nas regras
        def novaTransicao(self, texto, regra):
            self.Alfabeto.add(texto);                                               # Adiciona o símbolo no alfabeto

            if regra not in regras:                                                 # Se a regra ainda não foi mapeada:
                novaRegra(self, regra);                                             # Cria a regra nova

            if texto in estados[regraAtiva]:                                        # se o símbolo já existe no estado:
                lista = list(set(estados[regraAtiva][texto] + [regras[regra]]));    # Adiciona o simbolo novo
                estados[regraAtiva][texto] = lista;                                 # aos existentes.

            else:                                                                   # Senao
                estados[regraAtiva].update({texto: [regras[regra]]});               # Adiciona o símbolo no estado.


        for linha in textos:                                                    # Faz um loop nas linhas do texto de entrada
            
            linha = linha.replace('|', '/')
            word = '';                                                          # Zera a palavra

            for caractere in linha:                                             # Faz um loop nos caracteres da linha
                if caractere in ignorar:                                        # Se o caractere estiver na lista de ignorados:
                    continue;                                                   # Não faz nada

                word = word + caractere;                                        # Concatena a palavra com o caractere válido

                if re.match('<\S>', word) is not None:                          # Se a palavra tem o formato de um nome de regra:
                    if word[1] not in regras:                                   # Se não existe regra com esse nome:
                        novaRegra(self, word[1]);                               # Adiciona a nova regra com esse nome.
                    regraAtiva = regras[word[1]];                               # Marca a flag de regra ativa para adicionar uma transição nessa regra
                    word = '';                                                  # Reinicia a palavra

                elif (re.match('/\S<\S>', word) is not None or
                      re.match('=\S<\S>', word) is not None):                   # Se a palavra tem o formato de uma transição:
                    novaTransicao(self, word[1], word[3]);                      # Adiciona uma nova transição à regra ativa
                    word = '';                                                  # Reinicia a palavra

                elif (re.match('/<\S>', word) is not None or                    
                      re.match('=<\S>', word) is not None):                     # Se a palavra tem o formato de um nome de regra:
                    novaTransicao(self, EPSILON, word[2]);                        # Adiciona uma nova transição à regra ativa
                    word = '';                                                  # Reinicia a palavra

                elif ((word == '/' + FINAL) or (word == '=' + FINAL)):                                             # Se foi encontrado um caractere que indica estado final:
                    self.Finais.add(regraAtiva);                                # Marca a regra ativa como final.

            self.insereEstadosGramatica(estados);                               # Insere os estados criados localmente nos estados do automato


    # -- Inserção das regras da gramática regular no automato
    def insereEstadosGramatica(self, estados):        
        for nome, estado in estados.items():                                        # Faz um loop no estado temporário
            self.setAlfabetoEstado(estado);
            for simbolo, transicoes in estado.items():                              # Faz um loop no transições do estado temporário
                if nome not in self.Estados:                                        # Se o nome/número do estado não existe no automato:
                    self.Estados.update({nome: {}});                                # Adiciona o estado ao automato

                if simbolo in self.Estados[nome]:                                   # Se o símbolo já existe no estado:
                    lista = list(set(self.Estados[nome][simbolo] + transicoes));    # Adiciona as transições do estado temporário
                    self.Estados[nome][simbolo] = lista;                            # Junto às transições do estado do automato

                else:                                                               # Senão:
                    self.Estados[nome].update({simbolo: transicoes});               # Adiciona as novas transições no estado.


    # -- Imprime o automato finito deterministico
    def imprimir(self, mensagem = ''):
        print(mensagem)
        estados = self.pegarAutomato();
        for nome, estado in sorted(estados.items()):                   # Faz um loop nos estados
            print(' *' if nome in self.Finais else '  ', end='');   # Marca os estados que são finais
            print(nome, end=' = ');                                 # Imprime o nome/numero do estado

            for simbolo, transicoes in estado.items():              # Faz um loop em cada estado
                
                if len(transicoes) > 0:                             # Se existir transições para um símbolo
                    print(simbolo, transicoes, end=', ');           # Imprime o símbolo e a lista de transições

            print('');                                              # Insere uma quebra de linha ao final de cada impressão de símbolo


    # -- Insere todos os símbolos do alfabeto em um estado
    def setAlfabetoEstado(self, estado):
        for simbolo in sorted(self.Alfabeto):   # Faz um loop nos símbolos do alfabeto da linguagem
            if simbolo not in estado:           # Se o símbolo não existir no estado:
                estado.update({simbolo: []});   # Adiciona o símbolo associado à uma lista vazia.


    # -- Relacioana os estados com os símbolos do alfabeto
    def setAlfabeto(self):
        for nome, estado in self.Estados.items():   # Faz um loop nos estados
            self.setAlfabetoEstado(estado);         # Relacioana o estado com os símbolos do alfabeto


    # -- Insere no automato:
    def carrega(self):
        new = True;                                     # Marca flag de novo estado

        self.Estados.update({len(self.Estados): {}});   # Inicializa o estado inicial com: um inteiro para chave e um dicionário vazio para conteúdo

        for simbolo in self.Texto:                      # Faz um loop, caractere e caractere na string da estrada
            simbolo = simbolo.lower();                  # Utiliza todas as letras em minusculo

            if simbolo == '\n':                         # Identifica quebra de linha
                if new:                                 # Se houve duas quebras de linha seguidas:
                    break;                              # Termina a leitura de tokens
                new = True;                             # Marca flag para informar que o próximo símbolo é o início de um novo token
                self.Finais.add(len(self.Estados) - 1); # Adiciona a informação de estado final em um estado

            else:                                       # Se não for quebra de linha:
                self.carregaToken(simbolo, new);        # Carrega o token para o autômato.
                new = False;                            # Reseta a variável para o próximo símbolo

        texto = self.Texto.partition('\n\n')[2];        # Separa o texto após as duas quebras de linha para a leitura de gramática
        self.carregaGramatica(texto.splitlines());      # Envia o texto em formato de lista com as linhas do texto
        self.setAlfabeto();                             # Relaciona os estados com o alfabeto da linguagem


    # -- Determiniza um estado do automato
    def determinizar(self, producoes):        
        estadoTemporario = dict();                                                  # Cria um estado temporário
        #novoEstado = len(self.Estados);                                             # Dá nome/número ao estado que será criado
        #producoes = transicoes;
        producaoAgrupada = self.geraProducaoAgrupada(producoes); 

        #if producaoAgrupada in self.NovasProducoes:
        #    self.Estados[transicao][producao] = [self.NovasProducoes[producaoAgrupada][0]];

        if ((producaoAgrupada not in self.NovasProducoes) or (self.NovasProducoes[producaoAgrupada][0] not in self.Estados)):            
            if (len(producoes) > 1) and (not self.existeProducaoAgrupada(producoes)):
                novoEstado = self.pegarNovoEstadoDetrminizacao();
                self.NovasProducoes.update({self.geraProducaoAgrupada(producoes): [novoEstado,producoes]});
            for i in producoes:                                                         # Faz um loop nas produções que que contém a indeterminação
                for j in sorted(self.Alfabeto):                                         # Faz um loop no conjunto de símbolos do alfabeto
                    if j in estadoTemporario:                                           # Se o o símbolo j já estiver no estado temporário:                        
                        lista = list(set(estadoTemporario[j] + self.pegarProducaoOriginal(self.Estados[i][j])));    # Adiciona a lista de transições de j
                        estadoTemporario[j] = lista;                                    # ao estado
                    
                        if (len(lista) > 1) and (not self.existeProducaoAgrupada(lista)):
                            novoEstado = self.pegarNovoEstadoDetrminizacao();
                            self.NovasProducoes.update({self.geraProducaoAgrupada(lista): [novoEstado,lista]});

                    else:
                        producaoAtual = list(set(self.Estados[i][j]));
                        
                        if len(producaoAtual) > 1:
                            producaoAgrupadaTemp = self.geraProducaoAgrupada(producaoAtual);
                            if self.existeProducaoAgrupada(producaoAgrupadaTemp):
                                estadoTemporario.update({j: list(set(self.NovasProducoes[producaoAgrupada][1]))});
                        
                        elif (len(producaoAtual) > 0) and (self.existeNovoEstado(producaoAtual[0])):
                            for prod in self.NovasProducoes:
                                if self.NovasProducoes[prod][0] == producaoAtual[0]:
                                    estadoTemporario.update({j: list(set(self.NovasProducoes[prod][1]))});
                        else:
                            estadoTemporario.update({j: producaoAtual});
        
            self.setAlfabetoEstado(estadoTemporario);                                   # Relaciona o estado temporário com os símbolos do alfabeto                    
            self.Estados.update({self.NovasProducoes[producaoAgrupada][0]: estadoTemporario});                        # Adiciona o estado temporário ao dicionário de estados da classe
            self.adicionaEstadoFinal(producoes, self.NovasProducoes[producaoAgrupada][0]);
            self.substituiNovaProducao();

        return;


    def adicionaEstadoFinal(self, producoes, novaProducao):
        for producao in producoes:
            if producao in self.Finais:
                self.Finais.add(novaProducao);


    def pegarProducaoOriginal(self, producaoOrig):
        retorno = list(set(producaoOrig));
        for producao in self.NovasProducoes:
            for prod in producaoOrig:
                if self.NovasProducoes[producao][0] == prod:
                    retorno = list(set(self.NovasProducoes[producao][1]));

        return retorno;


    def pegarNovoEstadoDetrminizacao(self):
        novasProducoes = [];
        for producao in self.NovasProducoes:
            novasProducoes.append(self.NovasProducoes[producao][0]);

        return len(set(list(self.Estados) + novasProducoes));
    

    def geraProducaoAgrupada(self, lista):
        estado = '';
        for item in lista:
            if estado == '':
                estado += str(item);
            else:
                estado += ',' + str(item);

        return estado;


    def substituiNovaProducao(self):
        if len(self.NovasProducoes) > 0:            
            for transicoes in self.Estados:
                for letra in sorted(self.Alfabeto): 
                    if len(self.Estados[transicoes][letra]) > 1:
                        producaoAgrupadaTemp = self.geraProducaoAgrupada(self.Estados[transicoes][letra]);
                        if producaoAgrupadaTemp in self.NovasProducoes:
                            self.Estados[transicoes][letra] = [self.NovasProducoes[producaoAgrupadaTemp][0]];


    def existeProducaoAgrupada(self, lista):
        retorno = False;

        if len(lista) > 1:
            producaoAgrupadaTemp = self.geraProducaoAgrupada(lista);
            return (producaoAgrupadaTemp in self.NovasProducoes);
        else:
            for i in self.NovasProducoes:
                if lista[0] in self.NovasProducoes[i][1]:
                    return True;
        return retorno;


    def existeNovoEstado(self, producao):
        if len(self.NovasProducoes) > 0:
            for producaoAgrupada in self.NovasProducoes:
                if self.NovasProducoes[producaoAgrupada][0] == producao:
                    return True;

        return False;

                        
    # -- Percorre o autômato identificando e tratando seus indeterminismos
    def buscarIndeterminismo(self):
        qtdEstados = len(self.Estados);                                         # Marca a quantidade inicial de estados do autômato
        i = 0;                                                                  # Zera a variável de índice
        while i < qtdEstados:                                                   # Faz um loop pelos estados
            for j in sorted(self.Alfabeto):                                     # Itera um laço pelo conjunto de símbolos do alfabeto
                if i in self.Estados and len(self.Estados[i][j]) > 1:           # Se houver uma transição estiver indeterminada:
                    self.determinizar(self.Estados[i][j]);                                     # Determiniza o estado

                    qtdEstados = len(self.Estados);                             # Atualiza a quantidade de estados
            i += 1;                                                             # Incrmenta o índice.
            
            if i == qtdEstados:
                for novoEstado in list(self.NovasProducoes):
                    if self.NovasProducoes[novoEstado][0] not in self.Estados:
                        self.determinizar(self.NovasProducoes[novoEstado][1]); 
                        qtdEstados = len(self.Estados); 


    def buscarEpsilonTransicoes(self):        
        if EPSILON not in self.Alfabeto:
            return

        producoesComEpsilon = set();
        qtdEpsilon = len(producoesComEpsilon);
        qtdEstados = len(self.Estados); 
        idxEpsilon = self.Alfabeto
        i = 0;

        while i < qtdEstados:                                                                       # Faz um loop pelos estados
            if i in self.Estados and len(self.Estados[i][EPSILON]) > 0:                             # Se houver uma transição com épsion
                self.removerEpsilonTransicoes(i, self.Estados[i][EPSILON][0], producoesComEpsilon);
                qtdEstados = len(self.Estados);                                                     # Atualiza a quantidade de estados
            i += 1;

        self.removerEpsilonTransicoesEstados();


    def removerEpsilonTransicoes(self, transicaoOriginal, transicaoEpsilon, producoesComEpsilon):
        if len(self.Estados[transicaoOriginal][EPSILON]) > 0:

            for producao in list(self.Estados[transicaoEpsilon]):
                if producao != EPSILON and len(self.Estados[transicaoEpsilon][producao]) > 0:                    
                    self.Estados[transicaoEpsilon][producao] = (list(set(self.Estados[transicaoEpsilon][producao] + self.Estados[transicaoOriginal][producao])));                    
                    producoesComEpsilon.update(set(self.Estados[transicaoOriginal][EPSILON]));                    
        
        if len(self.Estados[transicaoEpsilon][EPSILON]) > 0:            
            if self.Estados[transicaoEpsilon][EPSILON][0] not in producoesComEpsilon:
                self.removerEpsilonTransicoes(transicaoEpsilon, self.Estados[transicaoEpsilon][EPSILON][0], producoesComEpsilon);


    def removerEpsilonTransicoesEstados(self):
        if EPSILON not in self.Alfabeto:
            return
        
        qtdEstados = len(self.Estados); 
        i = 0;
        
        while i < qtdEstados:                           # Faz um loop pelos estados
            if i in self.Estados:                       # Se houver uma transição com Épsilon
                self.Estados[i].pop(EPSILON);           # Remove as produções do Épsilon
                qtdEstados = len(self.Estados);         # Atualiza a quantidade de estados
            i += 1;

        self.Alfabeto.remove(EPSILON);


    def removerInalcancaveis(self):
        estados = self.gerarEstadosParaMinimizacao();
        self.visitaNovaProducaoInalcancavel(estados, 0);


    def visitaNovaProducaoInalcancavel(self, estados, transicao):
         if transicao in estados:
             for producao in estados[transicao]:
            
                if not estados[transicao][producao].temProducao():        #caso não tenha uma produção válida
                    continue;
            
                if estados[transicao][producao].visitado:
                    return;
        
                estados[transicao][producao].visitado = True;
                self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao);
                self.visitaNovaProducaoInalcancavel(estados, estados[transicao][producao].producao);            


    def adicionaAutomatoMinimizado(self,transicao,producaoAtual,producaoInserir):
        if transicao not in self.AutomatoMinimizado:
            self.AutomatoMinimizado.update({transicao : {producaoAtual: [producaoInserir]}});
        else:
            if producaoAtual not in self.AutomatoMinimizado[transicao]:
                self.AutomatoMinimizado[transicao].update({producaoAtual: [producaoInserir]});        


    #atualmente esta lista temp não esta clonando, as referencias com o original permanecem, precisa criar nova estrutura;
    def gerarEstadosParaMinimizacao(self):
        estadosTemp = dict();
        AutomatoValido = self.pegarAutomato();

        for transicao in AutomatoValido:
            for producao in list(AutomatoValido[transicao]):
                if len(AutomatoValido[transicao][producao]) > 0:
                    if transicao not in estadosTemp: #--
                        estadosTemp.update({transicao : {producao: Producao(AutomatoValido[transicao][producao][0])}});
                    else:
                        if producao not in estadosTemp[transicao]:
                            estadosTemp[transicao].update({producao: Producao(AutomatoValido[transicao][producao][0])});
                else:
                    if ((transicao in estadosTemp) and (producao not in estadosTemp[transicao])):
                            estadosTemp[transicao].update({producao: Producao(-1)});

        return estadosTemp;


    def pegarAutomato(self):
        if len(self.AutomatoMinimizado) > 0:
            return self.AutomatoMinimizado;
        else:
            return self.Estados;


    def removerMortos(self):
        estados = self.gerarEstadosParaMinimizacao();
        self.TransicoesVisitadas = [];
        self.AutomatoMinimizado = dict();

        for transicao in estados:
            for producao in estados[transicao]:
                self.visitaNovaProducaoMortos(estados, transicao);
                estados[transicao][producao].chegouEstadoTerminal = self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao);
        

    def visitaNovaProducaoMortos(self, estados, transicao):
        #self.TransicoesVisitadas = list(set([transicao] + self.TransicoesVisitadas));
        if transicao in estados:     
            for producao in estados[transicao]:            

                if estados[transicao][producao].chegouEstadoTerminal or (transicao in self.Finais):
                    return True;            
            
                if not estados[transicao][producao].temProducao():        #caso não tenha uma produção válida
                    return False;

                if estados[transicao][producao].visitado:
                    continue;

        
            estados[transicao][producao].visitado = True;
                       
            
            if self.visitaNovaProducaoMortos(estados, estados[transicao][producao].producao):
                estados[transicao][producao].chegouEstadoTerminal = True;
                self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao);
                return True;

        return False;

