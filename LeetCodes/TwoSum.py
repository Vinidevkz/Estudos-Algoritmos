# Made by Vinicius Eduardo 09/12/2024, Brazil, São Paulo
# LeetCode: TwoSum
# Lenguage: Python



#O(n²)
myList = [2, 3, 4, 7]

# def twoSum(List, number):
#      low = 0 #the lowest index on the list
#      high = len(myList) -1 #the highest index on the list
#      for low in range(len(myList)): #repeat low until you don't reach the end of the list
#          for high in range(len(myList)): #repeat high until you don't reach the end of the list
#              if(myList[low] + myList[high] == number): #if the lowest index plus highest index equal a our target number,
#                  return[low, high] #it returned teh index's
#              else:
#                  high = myList[high] -1 #else, the high will receive himself minus one


# print("Result:", twoSum(myList, 9))


#O(n)
def twoSum2(List2, target):
      dictionary = {} #create an empty dictionary to store seen number and their indices
      for i, num in enumerate(List2):
         complement = target - num
         if complement in dictionary:
            return[dictionary[complement], i]
         dictionary[num] = i
      return[]

print(twoSum2(myList, 5))


