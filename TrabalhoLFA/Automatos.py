class Automato(object):

    Estados = dict();

    # -- Leitura de arquivos:
    def __init__(self, arquivo):

        self.Estados = {};  # Inicializa o dictionary da classe

        arquivo = open(arquivo, 'r');   # Abre o arquivo de entrada
        texto = arquivo.read();         # Lê o arquivo de entrada
        self.carrega(texto);            # Carrega o automato a partir do arquivo de texto

    # -- Inserção no automato:
    def carrega(self, texto):

        New = True;

        self.Estados.update({len(self.Estados):{}});

        for a in texto:
            a = a.lower();  # Utiliza letra em minusculo
           
            if a == '\n':   # Identifica quebra de linha
                New = True; # Flag de nova palavra
            else:
                if New:
                    if a in self.Estados[0]:                                # Se o Token já existe no estado
                        self.Estados[0][a].append(len(self.Estados));       # Então adiciona referenciando o token
                    else:
                        self.Estados[0].update({a: [len(self.Estados)]});   # Senão carrega no estado inicial, criando novo token

                    self.Estados.update({len(self.Estados):{}});            # Cria o próximo estado para continuação
                    New = False;
                else:
                    self.Estados[len(self.Estados) - 1].update({a: [len(self.Estados)]});   # Insere no último estado criado
                    self.Estados.update({len(self.Estados):{}});                            # Cria o próximo estado para continuação


                

