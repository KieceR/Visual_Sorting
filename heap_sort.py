def heap_sort(lista):
    n = len(lista)
    for i in range(n//2 -1, -1, -1):
        montar_heap(lista, n, i)
    for i in range(n-1, -1, -1):
        lista[0], lista[i] = lista[i], lista[0]
        montar_heap(lista, i, 0)

def montar_heap(lista, n, i):
    maior = i
    esquerda = 2*i + 1
    direita = 2*i + 2
    if esquerda < n and lista[maior] < lista[esquerda]:
        maior = esquerda
    if direita < n and lista[maior] < lista[direita]:
        maior = direita
    if maior != i:
        lista[i], lista[maior]= lista[maior], lista[i]

        
