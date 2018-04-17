import random

lista_continua = []

for i in range(500):
	lista_continua.append(i)

lista_randomizada = lista_continua

random.shuffle(lista_randomizada)

lista_ordenada = lista_randomizada

'''

for j in range(len(lista_ordenada)-1):
	switch = False
	for i in range(len(lista_ordenada)-j-1):
		if lista_ordenada[i] > lista_ordenada[i+1]:
			lista_ordenada[i], lista_ordenada[i+1] = lista_ordenada[i+1], lista_ordenada[i]
			switch = True
	if not switch:
		break

'''

print(lista_randomizada)