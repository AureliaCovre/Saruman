# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais
# para calcular o ICM, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos 

entrada = input("Insira aqui: ").split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

resultado = distancia / (diametro1 + diametro2) 

print("{:.2f}".format(resultado))