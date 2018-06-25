import re

class Automato(object):
    
    # -- Declaração dos campos da classe
    Estados = dict();   # Estrutura que guarda todos os estados do autômato
    Alfabeto = set();   # Estrutura que contém todos os símbolos do alfabeto
    Texto = str();      # Campo para guardar a string de entrada


    # -- Inicialização da classe:
    def __init__(self, arquivo):
        self.Estados = dict();          # Inicializa o dictionary de estados com uma estrutura vazia
        self.Alfabeto = set();          # Inicializa o set do alfabeto com uma estrutura vazia

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



    # -- Inserção das regras da Gramática Regular
    def carregaGramatica(self, textos):
        regras = dict();
        estados = dict();

        ignorar = [' ', ':', '=', '|'];


        def novaRegra(self, texto):
            if texto == 'S':
                regras.update({'S': 0});
                estados.update({0: {}})
            else:
                numero = len(self.Estados) + len(regras) - 1;
                regras.update({texto: numero});
                estados.update({regras[texto]: {}})


        def novaTransicao(self, texto, regra):
            self.Alfabeto.add(texto);
            if regra not in regras:
                novaRegra(self, regra);
            estados[regraAtiva].update({texto: [regras[regra]]});


        for linha in textos:
            word = '';
            for caractere in linha:
                if caractere in ignorar:
                    continue;

                word = word + caractere;
    
                if re.match('<\S>', word) is not None:
                    if word[1] not in regras:
                        novaRegra(self, word[1]);
                    regraAtiva = regras[word[1]];
                    word = '';

                elif re.match('\S<\S>', word) is not None:
                    novaTransicao(self, word[0], word[2]);
                    word = '';

            self.insereEstadosGramatica(estados);


    def insereEstadosGramatica(self, estados):
        for nome, estado in estados.items():
            for simbolo, transicoes in estado.items():
                if nome not in self.Estados:
                    self.Estados.update({nome: {}});    

                if simbolo in self.Estados[nome]:
                    lista = list(set(self.Estados[nome][simbolo] + transicoes));
                    self.Estados[nome][simbolo] = lista;
                else:
                    self.Estados[nome].update({simbolo: transicoes});
            



    # -- Imprime o automato finito deterministico
    def imprimir(self):
        for nome, estado in self.Estados.items():                   # Faz um loop nos estados
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

            else:                                       # Se não for quebra de linha:
                self.carregaToken(simbolo, new);        # Carrega o token para o autômato.
                new = False;                            # Reseta a variável para o próximo símbolo

        texto = self.Texto.partition('\n\n')[2];        # Separa o texto após as duas quebras de linha para a leitura de gramática
        self.carregaGramatica(texto.splitlines());      # Envia o texto em formato de lista com as linhas do texto
        self.setAlfabeto();                             # Relaciona os estados com o alfabeto da linguagem


    # -- Determiniza um estado do automato
    def determinizar(self, producoes):
        estadoTemporario = dict();                                                              # Cria um estado temporário
        novoEstado = len(self.Estados);                                                         # Dá nome/número ao estado que será criado

        for i in producoes:                                                                     # Faz um loop nas produções que que contém a indeterminação
            for j in sorted(self.Alfabeto):                                                     # Faz um loop no conjunto de símbolos do alfabeto
                if j in estadoTemporario:                                                       # Se o o símbolo j já estiver no estado temporário:
                    estadoTemporario[j] = list(set(estadoTemporario[j] + self.Estados[i][j]))   # Adiciona a lista de transições de j ao estado
                else:                                                                           # Senão:
                    estadoTemporario.update({j: list(set(self.Estados[i][j]))});                # Atualiza o estado temporário com o símbolo j e com a lista já existente no estado

        self.setAlfabetoEstado(estadoTemporario);                                               # Relaciona o estado temporário com os símbolos do alfabeto
        self.Estados.update({novoEstado: estadoTemporario});                                    # Adiciona o estado temporário ao dicionário de estados da classe
        
        return [novoEstado];                                                                    # Renorna o nome/número do estado adicionado


    # -- Percorre o autômato identificando e tratando seus indeterminismos
    def buscarIndeterminismo(self):
        qtdEstados = len(self.Estados);                                         # Marca a quantidade inicial de estados do autômato
        i = 0;                                                                  # Zera a variável de índice
        while i < qtdEstados:                                                   # Faz um loop pelos estados
            for j in sorted(self.Alfabeto):                                     # Itera um laço pelo conjunto de símbolos do alfabeto
                if len(self.Estados[i][j]) > 1:                                 # Se houver uma transição estiver indeterminada:
                    self.Estados[i][j] = self.determinizar(self.Estados[i][j]); # Determiniza o estado

                    qtdEstados = len(self.Estados);                             # Atualiza a quantidade de estados
            i += 1;                                                             # Incrmenta o índice.
