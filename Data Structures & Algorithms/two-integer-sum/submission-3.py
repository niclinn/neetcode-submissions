class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {} # num: index
        for i in range(len(nums)): 
            num = nums[i]
            if target - num in numSet: 
                return [numSet[target - num], i]
            numSet[num] = i