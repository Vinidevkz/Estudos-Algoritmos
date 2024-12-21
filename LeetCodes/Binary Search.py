#Pesquisa Binária - Cap 1
#Feito por Vinicius Eduardo, 2024

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        baixo = 0
        alto = len(nums) -1


        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = nums[meio]

            if chute == target:
                return meio
            elif chute > target:
                alto = meio - 1
            else:
                baixo = meio + 1
        return -1