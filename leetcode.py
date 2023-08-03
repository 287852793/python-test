from typing import *

# leetcode 1984
# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         if nums == None or len(nums) < 2:
#             return 0
#         nums.sort()
#         t = nums[k - 1] - nums[0]
#         for i in range(k, len(nums)):
#             if nums[i] - nums[i - k + 1] < t:
#                 t = nums[i] - nums[i - k + 1]
#         return t

# t = Solution()
# nums = [9, 4, 1, 7]
# k = 2
# r = t.minimumDifference(nums, k)
# print(r)

# leetcode 713
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k == 0 or k == 1:
#             return 0
#         a = b = r = 0
#         s = 1
#         for b in range(0, len(nums)):
#             s *= nums[b]
#             while s >= k:
#                 s /= nums[a]
#                 a = a + 1
#             r += b - a + 1
#         return r

# t = Solution()
# nums = [10, 5, 2, 9]
# k = 100
# r = t.numSubarrayProductLessThanK(nums, k)
# print(r)

# leetcode 2144
# class Solution:
#     def minimumCost(self, cost: List[int]) -> int:
#         cost = sorted(cost)
#         t = 1
#         r = 0
#         for i in range(len(cost) - 1, -1, -1):
#             if t % 3 != 0:
#                 r += cost[i]
#             t++
#         return r

# leetcode 1299
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         m = -1
#         for i in range(len(arr) - 1, -1, -1):
#             arr[i] = m
#             m = max(m, arr[i])
#         return arr

# leetcode 2139
# class Solution:
#     def minMoves(self, target: int, maxDoubles: int) -> int:
#         r = 0
#         while target > 0 and maxDoubles > 0:
#             if target % 2 == 1:
#                 target = target - 1
#             else:
#                 target = target / 2
#                 maxDoubles = maxDoubles - 1
#             r = r + 1
#         r = r + target - 1
#         return r


# leetcode 2408
# class Solution:

#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[0] * m for i in range(n)]
#         dp[0][0] = grid[0][0]
#         print(dp)
#         for i in range(1, m):
#             dp[i][0] = dp[i - 1][0] + grid[i][0]
#         for i in range(1, n):
#             dp[0][i] = dp[0][i - 1] + grid[0][i]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
#         return dp[m - 1][n - 1]

# t = Solution()
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# r = t.minPathSum(grid)

# print(r)

# leetcode 881
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r, i, j = 0, 0, len(people) - 1
        while i < j:
            t = limit - people[i]
            if people[j] <= t:
                i = i + 1
            r = r + 1
            j = j - 1
        if i == j:
            r = r + 1
        return r
                
                

