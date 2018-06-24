class Automato(object):

    Estados = dict();
    Alfabeto = set();

    # -- Leitura de arquivos:
    def __init__(self, arquivo):

        self.Estados = {};  # Inicializa o dictionary da classe

        arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
        texto = arquivo.read();         # Lê o arquivo de entrada
        self.carrega(texto);            # Carrega o automato a partir do arquivo de texto

        self.setAlfabeto();             # Relacioanar os estados com o Alfabeto

        self.imprimir();                # Imprimir 


    # -- Inserção de Tokens da Linguagem
    def carregaTokens(self, word, New):
        self.Alfabeto.add(word);
        if New:
            if word in self.Estados[0]:                                # Se o Token já existe no estado
                self.Estados[0][word].append(len(self.Estados));       # Então adiciona referenciando o token
            else:
                self.Estados[0].update({word: [len(self.Estados)]});   # Senão carrega no estado inicial, criando novo token

            self.Estados.update({len(self.Estados):{}});            # Cria o próximo estado para continuação
        else:
            self.Estados[len(self.Estados) - 1].update({word: [len(self.Estados)]});   # Insere no último estado criado
            self.Estados.update({len(self.Estados):{}});                            # Cria o próximo estado para continuação


    # -- Inserção das regras da Gramática Regular
    def carregaGramatica(self, word):
        pass


    def imprimir(self):
        for i in range(0, len(self.Estados)): 
            print(i, end=' = ')
            for j in sorted(self.Alfabeto):
                if len(self.Estados[i][j]) > 0:
                    print(j, self.Estados[i][j], end=', ');
            print('')


    # -- Relacioanar os estados com o Alfabeto
    def setAlfabeto(self):
        for i in range(0, len(self.Estados)):  
            for j in self.Alfabeto:
                if j not in self.Estados[i]:
                    self.Estados[i].update({j:[]})
            
        

    # -- Inserção no automato:
    def carrega(self, texto):

        New = True;

        self.Estados.update({len(self.Estados):{}});

        for a in texto:
            a = a.lower();  # Utiliza letra em minusculo
           
            if a == '\n':   # Identifica quebra de linha
                New = True;
                #self.carregaGramatica(a);
            else:
                self.carregaTokens(a, New);
                New = False;



