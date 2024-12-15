#Pesquisa Binária - Cap 1
#Feito por Vinicius Eduardo, 2024


def palindromo(x):

    numero = x
    palindromo = ((x)[::-1])
    print("Numero normal: ", numero)
    print("Palíndromo", palindromo)   

    if palindromo == numero:
        return True
    else:
        return False
 

print(palindromo(123))
