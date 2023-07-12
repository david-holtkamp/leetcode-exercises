#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[i] + nums[j] == target): 
                    return [i, j]
        return "no numbers added equal target"

         
# @lc code=end
solution = Solution()
nums = [2,6,9,11]
target = 9 
result = solution.twoSum(nums, target)
print(result)