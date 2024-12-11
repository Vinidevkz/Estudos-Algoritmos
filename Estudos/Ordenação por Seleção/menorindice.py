#Ordenação por seleção
#feito por Vinicius Eduardo, 2024
#
#Neste código encontraremos o menor elemento dentro de uma lista, ordenando ela. Nesse caso, queremos encontrar a música menos tocada.
#
#Notação do algoritmo(Big O): O(n)

musicas = [10, 10 , 7]

def pegarMenorIndice(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return(menor_indice)
print("Musica menos tocada:", pegarMenorIndice(musicas))