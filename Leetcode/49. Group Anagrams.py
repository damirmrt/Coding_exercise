'''
Создаем defaultdict чтобы не выдал ошибку когнда мы будем добавлять первый элеменнт
итерируемся по словам и для каждого слова создаем лист из нулей равный длине алфавита
для каждого сова итерируемся по буквам и заносим количекство букв в лист counter 
Далее лист counter в виде tuple идет в качестве ключа в hashmap а слово s идет в соответсвующее
value который из себя представляет list.

'''
from collections import defaultdict

class Solution:# O(m*n)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            res[tuple(counter)].append(s)

        return res.values()


class Solution1: # O(m*nlogn)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pairs = {}
        res = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in pairs:
                res[pairs[sorted_str]].append(s)
            else:
                pairs[sorted_str] = len(res)
                res.append([s])
        
        return sorted(res)