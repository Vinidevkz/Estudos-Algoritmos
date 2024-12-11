#Pesquisa Binária - Cap 1
#Feito por Vinicius Eduardo, 2024
#
#Neste algoritmo, temos um array de tamanho inderterminado, por ser incrivelmente lento nós percorrermos um array muito longo, por exemplo: de 1.000.000 de elementos,
#nós usamos a pesquisa binária, que consiste em ir dividindo esse array em dois, até encontrarmos o número que desejamos.


#Notação do algoritmo(Big O): O(log n)

def pesquisa_binaria(lista, item):
     baixo = 0
     alto = len(lista) -1

     while baixo <= alto:
         meio = (baixo + alto) // 2 # // retorna um numero inteiro, e / retorna um float
         chute = lista[meio]
         print("Ponto mais baixo:", baixo, "Ponto mais alto:", alto, "Meio:" ,meio)
         if chute == item:
             return meio
         if chute > item:
             alto = meio - 1
         else:
             baixo = meio + 1
     return None

minha_lista = [1, 3, 5, 7, 9, 11, 14]

print (pesquisa_binaria(minha_lista, 3)) # => 1
print (pesquisa_binaria(minha_lista, -1)) # => 1

#Exercícios
#1) Pesquisa binária em uma lista com 128 nomes (defina o log(n))
#R: 128 / 2 = 64 / 2 = 32 / 2 = 16 / 2 = 8 / 2 = 4 / 2 = 2 / 2 = 1, logo: log2(128) = 7
#2) Duplicando o tamanho da lista, qual é o número máximo
#R: 256 / 2 = 128 / 2 = 64 / 2 = 32 / 2 = 16 / 2 = 8 / 2 = 4 / 2 = 2 / 2 = 1, logo: log2(256) = 8