'''
Сначала создаем словарь а так же лист длиной равной len(nums) где каждый элемент лист
Прохордимся по nums и считаем количество элементов и заносим результаты в словарь
Далее из словаря переносим резулльтаты в наш список, при этом индекс списка будет равен частоте
 встречаемости a лист в этом списке будет состоять из значений в которые встречаются такое количество раз
nums = [1,2,5,2,2,2,7,7,7]
 
frequency =  [1,  2,  3,  4,  5,6,7,8,9]
             [1,5]   [7] [2]
Далее мы итьерируемся по этому списку с конца и заносим каждое число в res пока оно н7е станет равно k
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n, c in count.items():
            frequency[c].append(n)

        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    return res
