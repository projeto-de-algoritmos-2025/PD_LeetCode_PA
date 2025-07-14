from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(index: int) -> int:
            if index >= len(nums):
                return 0
            
            rob_current = nums[index] + dp(index + 2)
            skip_current = dp(index + 1)

            return max(rob_current, skip_current)
        
        return dp(0)
