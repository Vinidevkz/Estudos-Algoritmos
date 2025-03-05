# Made by Vinicius Eduardo 05/03/2025, Brazil, São Paulo
# LeetCode: Richest Customer Wealth
# Lenguage: Python

#declara a função que receberá um array
def maxWealthCustomer(array: list):
    #o valor máximo inicial é 0
    maxWealth = 0

    #inicia um for que percorre todo o array
    for i in range(len(array)):
        #soma o total do primeiro indice do array
        totalWealth = sum(array[i])
        #a função max pega o maior valor entre dois parametros, nesse caso
        #o valor máximo e o total calculado acima
        maxWealth = max(maxWealth, totalWealth)
    #retorna o valor máximo
    return maxWealth

customers = [[1, 2, 3], [3, 2, 0]]

print(maxWealthCustomer(customers))

#Primeira Execução do laço for:
# - o maxWealth é 0
# - ele soma o primeiro indice do array, nesse caso o array [1, 2, 3], total 6
# - verifica o maior valor entre o maxWealth e o totalWealth, nesse caso (0, 6)
# - seta o 6 dentro do maxWealth
#Segunda Execução do laço for:
# - o maxWealth é 6
# - ele soma o primeiro indice do array, nesse caso o array [3, 2, 0], total 5
# - verifica o maior valor entre o maxWealth e o totalWealth, nesse caso (6, 5)
# - seta o 6 dentro do maxWealth
##Por fim, retorna o maior valor, que no caso é o 6.