class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target-num
            if num in complementMap:
                return [complementMap[num],i]
            else:
                complementMap[complement] = i
    def bruteForseTwoSum(self,nums , target):
        for i in range(len(nums)):

           for j in range(i+1,len(nums)):

               sum = nums[i] + nums [j]
               if sum == target:
                  return [i,j]

