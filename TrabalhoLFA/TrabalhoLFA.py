from Producoes import Producoes
from Automato import Automato;

AutomatoCompleto = [];
New = True;

# -- Leitura de arquivos
arquivo = open('liguagem.txt', 'r');
texto = arquivo.read();


# -- Inserção no automato
AutomatoCompleto.append(Automato(0));

for a in texto:
    a = a.lower();  # Colocar letra em minusculo
    if a == '\n':   # Identificar quebras de linha
        New = True; # Flag de nova palavra
    else:
        if New:
            AutomatoCompleto[0].AddLigacao(a, len(AutomatoCompleto)); # Carrega no estado inicial
            AutomatoCompleto.append(Automato(len(AutomatoCompleto))); # Cria o estado para continuação
            New = False;
        else:
            AutomatoCompleto[-1].AddLigacao(a, len(AutomatoCompleto)); # Insere no último estado criado
            AutomatoCompleto.append(Automato(len(AutomatoCompleto)));  # Cria o estado para continuação 

# -- Impressão do Automato
for i in AutomatoCompleto:
    if len(i.Producoes) == 0:
        i.Final = True;
        print('*', end='');
    else:
        print(' ', end='');
    print('<' + str(i.Identificador) + '> ::= | ', end='');
    for j in i.Producoes:
        print(j.Token + '<' + str(j.Destino) + '> | ', end='');
    print('');


