#Pesquisa Binária - Cap 1
#Feito por Vinicius Eduardo, 2024

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        baixo = 0 #ponto mais baixo do array
        alto = len(nums) -1 #ponto mais alto do array


        while baixo <= alto: #enquanto o mais baixo for menor ou igual ao alto:
            meio = (baixo + alto) // 2 #o meio é o baixo (0) mais o alto dividio por 2, pegando o elemento do meio no array
            chute = nums[meio] #primeiro chute será com o elemento do meio

            if chute == target:
                return meio #se o primeiro chute for igual ao target, retorna o mesmo
            elif chute > target:
                alto = meio - 1 # se o chute for maior que o target, o alto agora será o meio menos 1, ignorando todo o resto da lista do meio pro final
            else:
                baixo = meio + 1 # se o chute for menor que o target, o baixo agora será o meio mais 1, ignorando todo o resto da lista do meio pro começo
        return -1