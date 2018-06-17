from Automato import Automato;


#Modelo de Utilização das estruturas;

AutomatoCompleto = [];

AutomatoCompleto.append(Automato('S'));
AutomatoCompleto[0].AddLigacao('a','A');
AutomatoCompleto[0].AddLigacao('b','S');
AutomatoCompleto[0].AddLigacao('a','NULL');

AutomatoCompleto.append(Automato('A'));
AutomatoCompleto[0].AddLigacao('a','A');
AutomatoCompleto[0].AddLigacao('b','A');
AutomatoCompleto[0].AddLigacao('b','NULL');
AutomatoCompleto[0].AddLigacao('NULL','NULL');

AutomatoCompleto[0].Ligacoes[0].Ativo = True;
AutomatoCompleto[0].Ligacoes[0].Destino = True;
AutomatoCompleto[0].Ligacoes[0].EhFinal = True;
AutomatoCompleto[0].Ligacoes[0].Inalcancavel = True;
AutomatoCompleto[0].Ligacoes[0].Morto = True;
AutomatoCompleto[0].Ligacoes[0].Visitado = True;

#------leitura de arquivos

arquivo = open('liguagem.txt', 'r');
texto = arquivo.read();
print(texto);
