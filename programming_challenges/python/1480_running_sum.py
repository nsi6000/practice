
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        value = 0
        result = []
        for n in nums:
            value += n
            result.append(value)
        return result
