#QuickSort - cap 4
#Feito por Vinicius Eduardo, 2025
#
#O QuickSort é um algoritmo de ordenação.

#Exemplo:
"""
def quicksort (array):
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

#1)
"""
def quicksort2(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[len(array) // 2]
        maiores = [i for i in array if i < pivo]
        iguais = [i for i in array if i == pivo]
        maiores = [i for i in array if i > pivo]
        return quicksort2(manores) + iguais + quicksort2(maiores)

print(quicksort2([numbers]))
"""
#2)
"""
def quicksort3(array):
    if len(array) < 2:
        return array
    else:
        for i in quicksort3([]):
            pivo = array[-1]
            menores = [i for i in array if i < pivo]
            iguais = [i for i in array if i == pivo]
            maiores = [i for i in array if i > pivo]
            return quicksort3(menores) + iguais + quicksort3(maiores)

print(quicksort3([10, 80, 30, 90, 40, 50, 70]))
"""

#3) sem recursão

def quicksortNoRe(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[-1]
        menores = [i for i in array if i < pivo]
        iguais = [i for i in array if i == pivo]
        maiores = [i for i in array if i > pivo]

        pilha = []
        pilha.append(maiores)
        pilha.append(menores)
        resultado = []

        while pilha:
            subArray = pilha.pop() #pega um subarray da pilha
            if len(subArray) > 1:
                p = subArray[-1]
                iguaisSub = [i for i in subArray if i == p]
                maioresSub = [i for i in subArray if i > p]
                menoresSub = [i for i in subArray if i < p]
                
                pilha.append(maioresSub)
                pilha.append(menoresSub)

                resultado.extend(menoresSub + iguaisSub + maioresSub)
            else:
                resultado.extend(subArray)
        return resultado
print(quicksortNoRe([5, 2, 1, 6, 9, 0, 3, 3]))
                



