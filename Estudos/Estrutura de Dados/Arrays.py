# Made by Vinicius Eduardo 26/02/2025, Brazil, São Paulo
# Arrays
# Lenguage: Python

#Estrutura básica:
cars = ['Fiat.', 'Jipe.', 'BMW.']

#Pegando um elemento do array:
x = cars[0] #primeiro elemento do array. Saída: Fiat

#Pegando o numero de elementos dentro deu array:
y = len(cars)
#print("Primeiro elemento: ", x, ". Número de Elementos: ", y)

#Loop dentro do array, listando todos os elementos:
for x in cars:
    print(x)

#Adicionando itens dentro de um array:
cars.append('Ford.')

#Removendo um item dentro de um array:
carro_retirado = cars.pop(1) #Saída: Jipe
cars.remove('BMW.') #Saída: [Fita, Jipe]
print('Carro retirado: ', carro_retirado, 'Outros Carros: ',  cars)
#Explicação: o método pop remove o índice e retorna o valor removido, já o remove deleta o primeiro valor expecificado, nesse caso 'BMW', mas não retorna nada.

##Métodos de um Array
cars.append()#Adiciona um elemento na lista
cars.clear()#Remove todos os elementos da lista
cars.copy()#Retorna uma cópia da lista
cars.count()#Retorna o numero de elementos com um valor específico. Exemplo: numeroDeFiats = cars.count('Fiat.') -> Saida: 1
cars.extend()#Adiciona os elementos da lista de qualquer iterável(lista, tupla, string, etc), no fim da lista atual. Exemplo: novaLista = cars.extend(['Uno', 'WVG'])
cars.index()#Retorna o index do primeiro elemento com o valor expecificado. Exemplo: primeiraBMW = cars.index('BMW') -> Saída: 2
cars.insert()#Adiciona um elemento em uma posição especifica. Exemplo: cars.insert(4, 'Fusca')
cars.pop()#Remove o elemento com base em sua posição do array e o retorna
cars.remove()#Remove o elemento do array com base em seu nome mas nao o retorna
cars.reverse()#Inverte a ordem da lista
cars.sort()#Ordena a lista, ou se colocar: cars.sort(reverse=True) - ele inverte a ordem da lista.


