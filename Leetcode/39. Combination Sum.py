'''
Time O(2^t)
Space O(t * 2^t)

'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) # включаем значение в решение
            cur.pop()
            dfs(i + 1, cur, total) # не включаем значение в решение

        dfs(0, [], 0)
        return res
        
