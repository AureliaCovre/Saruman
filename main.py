""" Projeto Saruman - Desafio de código DIO
Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao senhor do mal, Sauron. 
Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos
Nazgûl (antigos reis humanos que foram contaminados pelos poderes dos anéis de Sauron). Saruman comandou a torre 
de Orthanc, onde cria seus servos Uruk-hai, orcs mais visíveis que os ocasionais. Para comunicação, eles utilizam
as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres. A Terra-média avança cada vez mais em 
tecnologia, muito impulsionada pelas guerras que acometem diariamente. Um dos problemas que tem atrapalhado sua 
população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidade de Gondor, 
concluíram que para calcular o ICM para Palantír's, basta dividir a distância entre os dois Palantír's, pela soma 
do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito 
sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido. Saruman e Sauron precisam de uma 
comunicação estável, pois têm medo de que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem 
saber quanto de ICM há na comunicação de seus Palantír, para que saibam quanto de magia deve ser empregada na 
comunicação.

Entrada: A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman. Saída: Um valor real descer o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.

Entrada: 100 2 2 | Saída: 25h00 Entrada: 200 3 8 | Saída: 18h18

IX Olimpíada Interna de Programação do IFSULDEMINAS - OLIP 2019   """

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais
# para calcular o ICM, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos 

entrada = input("Insira aqui: ").split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

resultado = distancia / (diametro1 + diametro2) 

print("{:.2f}".format(resultado))