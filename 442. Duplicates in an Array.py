# Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            n = abs(n)
            if nums[n-1]>0: nums[n-1] *= -1
            else: result.append(n)
        return result
