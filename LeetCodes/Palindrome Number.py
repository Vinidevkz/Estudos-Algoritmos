# Made by Vinicius Eduardo 09/12/2024, Brazil, São Paulo
# LeetCode: Palindrome Number
# Lenguage: Python


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
