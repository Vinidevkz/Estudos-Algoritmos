#QuickSort - cap 4
#Feito por Vinicius Eduardo, 2025
#
#A estratégia Dividir para conquistar é um algoritmo recursivo, ou seja, chama a si mesmo dentro de sua função. a idéia
#é dividir o problema para que ele se torne o menor possível (caso base), assim reduzindo sua dificuldade.abs

def soma(lista):
    numeros = lista

    prim = numeros[0]
    print("Primeiro numero:", prim)
    resto = numeros[1:]
    print("Resto da lista:", resto)

    total = prim + sum(resto)
    return total

numeros = [1, 2, 3]
print("Total:",soma(numeros))