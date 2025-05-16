class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}
        frequency = [[] for i in range(len(words) + 1)]
        res = []
        for word in words:
            count[word] = 1 + count.get(word, 0)
        
        for word, freq in count.items():
            frequency[freq].append(word)
        
        for i in range(len(frequency) - 1, -1, -1):
            if k == 0:
                break
            while frequency[i] and k != 0:
                res.append(frequency[i].pop())
                k -= 1
        
        return sorted(res)
        
l = Solution()
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(l.topKFrequent(words, k))
