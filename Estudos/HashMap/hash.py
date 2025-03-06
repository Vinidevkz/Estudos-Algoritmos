#Hash Map
#feito por Vinicius Eduardo, 2025
#
#Uma tabela hash tem como propósito de organizar uma chave e um valor em uma tabela e, ao inserir
#uma das chaves, retorna o valor dela.
#
#Notação do algoritmo(Big O): O(1)


#Versão mais simples(verificação):
voted = {"Jorge": "55 anos", "Mike": "35 anos"}

def verifica_eleitor(nome):
    if voted.get(nome) :
        print(voted[nome])
    else:
        voted[nome] = True
        print("Usuário inexistente!")

print(verifica_eleitor("Jorge"))

