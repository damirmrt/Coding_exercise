'''
## Two Sums
nums = [1, 4, 6, 7, 9, 10, 3]
target = 16

d = {}


def f(nums, target):
    for i, j in enumerate(nums):
        r = target - j
        if r in d: return [d[r], i]
        d[j] = i

print(f(nums, target))
'''
import heapq

'''

# Remove element from list

nums = [0,1,2,2,3,0,4,2]
val = 2

def list(nums, val):
    i = 0
    for n in nums:
        if n != val:
            nums[i] = n
            i += 1
    return i, nums

print(list(nums, val))
'''
'''
nums = [0,1,2,2,3,0,4,2]
val = 2
i = 0
for n in nums:
    if n != val:
        nums[i] = n
        i+= 1
    else:
        nums.remove(val)
        nums.append('_')

print(nums)
'''

'''
# Search insert position

nums = [1,3,5,6]
target = 4

def list_insert(nums, target):
    if not nums:
        return 0

    for i, j in enumerate(nums):
        if j >= target:
            return i

    return len(nums)

print(list_insert(nums, target))

'''

'''
# Plus one

class Solution:
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif digits[-1] == 9 and len(digits) == 1:
            digits = [1,0]

            return digits
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits

digits = [9,9,9]

l = Solution()
print(l.plusOne(digits))

'''
'''
# Length of Last Word
s = "   fly me   to   the moon asd"
class Solution:
    def lengthOfLastWord(self, s):
        l = s.split()
        return len(l[-1])

sol = Solution()

print(sol.lengthOfLastWord(s))

'''
'''
# Longest common prefix
strs = ["flower","flow","floght"]
strs1 = ['f','flow', 'flflf']
class Solution:
    def longestCommonPrefix(self, strs):
        s_empty = ''
        for i in range(len(strs[0])): # итерируемся по буквам в первом слове
            for s in strs: # итерируемся по словам в листе
                if i == len(s) or s[i] != strs[0][i]: # s[i] первая буква в каждом слове, strs[0][i] первая буква в первом слове
                    return s_empty
            s_empty += strs[0][i]

        return s_empty

test = Solution()

print(test.longestCommonPrefix(strs1))

'''

'''
class Teather:
    def minmax_seats(self, seats):
        distance = 1
        maximum_distance = 0
        if len(seats) == 2:
            return distance
        else:
            for i in range(1,len(seats)):
                if seats[i] == 0:
                    distance += 1
                else:
                    if maximum_distance < distance:
                        maximum_distance = int(distance / 2)
                        distance = 1
                    else:
                        distance = 1

        return maximum_distance


seats = [1,0,0,0,1,0,1,0,0,0,0,0]
l = Teather()

print(l.minmax_seats(seats))

'''
'''
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

if j>=0:
    nums1[:k + 1] = nums2[:j + 1]

print(nums1)

'''

'''
Paskal Triangle

class Solution:
    def generate(self, numRows: int):
        l = []
        for i in range(numRows):
            l.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    l[i].append(1)
                else:
                    l[i].append(l[i-1][j-1]+l[i-1][j])

        return l


func = Solution()

print(func.generate(5))

'''
'''
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

prices = [7,5,4,3,1]


class Solution:
    def max_profit(self, prices: list):
        max_diff = 0
        best_price_to_by = prices[0]
        for price in prices:
            if price < best_price_to_by:
                best_price_to_by = price
            else:
                profit = price - best_price_to_by
                if profit > max_diff:
                    max_diff = profit


        return max_diff


l = Solution()
print(l.max_profit(prices))
'''

'''
# MEDIUM

#Input: prices = [7,1,5,3,6,4]
#Output: 7
#Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#Total profit is 4 + 3 = 7.

prices = [7,1,3,5,3,6,4]

class Solution:
    def max_total_profit(self, prices: list):
        total_profit = 0
        previous_price = prices[0]

        for price in prices:
            if price < previous_price:
                previous_price = price
            elif price > previous_price:
                profit = price - previous_price
                previous_price = price
                total_profit += profit

        return total_profit


l = Solution()
print(l.max_total_profit(prices))

'''
'''
s = "A man, a plan, a canal: Panama"
s = [i for i in s.lower() if i.isalnum()]

print(s == s[::-1])


'''

'''
class Solution:
    def getRow(self, rowIndex: int):
        l = []
        for i in range(rowIndex+1):
            l.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    l[i].append(1)
                else:
                    l[i].append(l[i - 1][j - 1] + l[i - 1][j])

        return l[rowIndex]

s = Solution()

print(s.getRow(3))
'''

'''
row = [1,0,0,0,1,0,1,0,0,0,0,0,0]

class Teather:
    def minmax_seats(self, seats):
        distance = 1
        max_distance = 0

        for seat in seats:
            if seat == 0:
                distance += 1
                if max_distance <= distance:
                    max_distance = distance
            else:
                distance = 1

        return max_distance // 2

l = Teather()

print(l.minmax_seats(row))

'''
'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        return d.values()

nums = [4,1,2,1,2]

l=Solution()

print(l.singleNumber(nums))

'''

'''
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        counter = 0
        median = nums[len(nums)//2]

        for num in nums:
            counter += abs(median-num)


        return counter

l = Solution()
nums = [1,0,0,8,6]

print(l.minMoves2(nums))

'''

'''
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        res = 0
        visited = set(())

        def search(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
                    i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visited:
                return 0

            visited.add((i,j))

            perim = search(i,j+1)
            perim +=search(i,j-1)
            perim +=search(i+1,j)
            perim +=search(i-1,j)
            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += search(i,j)
        return res
l = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(l.islandPerimeter(grid))
'''
'''
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set(())

        def search(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
                    i < 0 or j < 0 or grid[i][j] == "0" or (i, j) in visited:
                return 0

            visited.add((i, j))

            return (1 + search(i + 1, j) +
                    search(i - 1, j) +
                    search(i, j + 1) +
                    search(i, j - 1))

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if search(i, j) > 0:
                    counter += 1

        return counter

l = Solution()

print(l.numIslands(grid))

'''
'''
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int):
        visited = set(())

        def search(i, j):
            if i >= len(image) or j >= len(image[0]) or \
                    i < 0 or j < 0 or image[i][j] != image[sr][sc] or (i, j) in visited:
                return
            visited.add((i, j))

            image[i][j] = color

            search(i + 1, j)
            search(i - 1, j)
            search(i, j + 1)
            search(i, j - 1)

        search(())

        return image


l = Solution()

print(l.floodFill(image, sr, sc, color))

'''
'''
nums = [3, 2, 2, 0, 4]


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False

l = Solution()

print(l.canJump(nums))

'''
'''
nums = [2,3,5,1,4,1,1,2,4]

class Solution:
    def jump(self, nums: list[int]) -> int:
        counter = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest,i + nums[i])
            l = r+1
            r = farthest
            counter += 1

        return counter

l = Solution()

print(l.jump(nums))

'''
'''
intervals = [[1,3],[2,6],[8,10],[15,18],[16,22]]

class Solution:
    def merge(self, intervals: list[list[int]]):
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i+1][0]:
                intervals[i:i+2] = [[intervals[i][0],intervals[i+1][1]]]
                i += 1
            i+=1
        return intervals

l = Solution()

print(l.merge(intervals))

'''

''' 
def repr(self, group_start, group_end) -> str:
    # это просто правильно печатает группу

    if last_group_start == last_group_end:
        return str(last_group_end)

    return f'{last_group_start}-{last_group_end}'


def squeeze(numbers:list) -> str:
    if not numbers:  # граничный случай
        return ''

    numbers_ = sorted(numbers)  # сначала располагаем по порядку
    groups = []  # тут будем хранить группы

    last_group_start = numbers_[0]
    last_group_end = numbers_[0]

    for n in numbers_:
        # если предыдущая группа отличается от текущего числа на 1,
        # то это число входит в группу, то есть становится концом группы
        if last_group_end == n - 1:
            last_group_end = n

        # иначе мы понимаем, что группа закончилась,
        # мы её запоминаем и начинаем новую
        else:
            groups.append(last_group_start, last_group_end)
            last_group_start = n
            last_group_end = n

    # посленюю группу придётся обработать вручную
    groups.append(last_group_start, last_group_end))

    return ','.join(groups)


l = [1, 4, 5, 2, 3, 9, 8, 11, 0]

print(squeeze(l))

'''
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0, len(height)-1
        max_Q = 0
        while l < r:
            q = min(height[l],height[r])*(r-l)
            if max_Q < q:
                max_Q = q

            if height[l]<height[r]:
                l += 1
            else:
                r -= 1

        return max_Q

height = [1,8,6,2,5,4,8,3,7]

l = Solution()

'''
'''
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[1]*n for i in range(m)]
        for i in range(m-2, -1, -1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j] == 0 and\
                        obstacleGrid[i][j+1] == 0 and\
                        obstacleGrid[i+1][j] == 0 and\
                        obstacleGrid[m-1][n-1] == 0:
                    d[i][j] = d[i+1][j] + d[i][j+1]
                else:
                    continue
        return d[0][0]

l = Solution()

print(l.uniquePathsWithObstacles(obstacleGrid))

'''
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = 0
        res = 0

        for n in nums:
            if counter == 0:
                res = n
            counter += (1 if res == n else -1)


        return res

nums = [1,3,1,1,4,1,1,5,1,1,6,2,2]

l = Solution()

l.majorityElement(nums)

'''
'''
nums = [2,3,1,2,4,3]
target = 8

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums.sort()
        sub_sum = nums[-1]
        if sub_sum >= target:
            return 1

        for i in range(len(nums)-2, -1, -1):
            sub_sum += nums[i]
            if sub_sum >= target:
                return len(nums) - i
        return 0

l = Solution()
l.minSubArrayLen(target,nums)
'''
'''
nums = [2,1,1,1,20]

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1,rob2 = 0, 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

l = Solution()
l.rob(nums)
'''
'''
nums = [1,2,3,4,5,6,7]
k = 3

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        res = []
        res.extend(nums[len(nums) - k:])
        res.extend(nums[0:k])

        return print(res)

l = Solution()

l.rotate(nums,k)

W           E  
E       R   D 
A   B       Z
A           I     

'WECRLTEEEDROSEEEFOAAIVDEN'
'WECRLTEERDSOEEFEAOCAIVDEN'

'''


def timeConversion(s):
    day_part = s[-2:]
    time_val = s[:-2].split(sep=':')
    if day_part == "PM":
        time_val[0] = str(int(time_val[0]) + 12)

    return print(':'.join(time_val))

s = "07:05:45PM"

timeConversion(s)