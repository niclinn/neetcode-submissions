class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsMap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numsMap:
                return [numsMap[complement], i]

            numsMap[num] = i 