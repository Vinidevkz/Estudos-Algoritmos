#QuickSort - cap 4
#Feito por Vinicius Eduardo, 2025
#
#O QuickSort é um algoritmo de ordenação.

#Exemplo:
"""def quicksort (array):
    if len(array) < 2: #se o array for menor do que 2, ele retorna ele mesmo
        return array
    else:
        pivo = array[0] #definindo um pivo no array
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([1, 2, 3, 4, 5]))
"""

#Exercícios:
"""
def quicksort2(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[len(array) // 2]
        menores = [i for i in array if i < pivo]
        iguais = [i for i in array if i == pivo]
        maiores = [i for i in array if i > pivo]
        return quicksort2(menores) + iguais + quicksort2(maiores)

print(quicksort2([10, 14, 3, 0, 5, 2, 6, 9, 8, 11]))
"""

