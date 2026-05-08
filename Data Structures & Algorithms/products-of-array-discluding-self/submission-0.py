class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left, right = 1, 1
        
        for i, num in enumerate(nums): 
            res[i] = left
            left *= num
        
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= right
            right *= nums[i]
        
        return res