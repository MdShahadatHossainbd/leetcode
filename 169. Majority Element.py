class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        idx = 0
        count = 1
        for i in range(1, len(nums)):
            if (nums[i]==nums[idx]):
                count += 1
            else:
                count -= 1
            if (count == 0):
                idx = i
                count = 1
        return nums[idx]