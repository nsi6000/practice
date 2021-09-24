
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        anchor = 0
        
        for ii, i in enumerate(nums):
            if (ii > 0 and nums[ii-1] >= nums[ii]):
                anchor = ii
            result = max(result, ii - anchor + 1)
        
        return result
