# https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        y = x + 1
        while x < len(nums) - 1:
            if y >= len(nums):
                x += 1
                y = x + 1
            if nums[x] + nums[y] == target:
                return [x, y]
            else:
                x += 1
            
        return "There is no two sum."

print(Solution().two_sum([2,7,11,15], 9))
print(Solution().two_sum([3,2,4], 6))
print(Solution().two_sum([3,3], 6))
