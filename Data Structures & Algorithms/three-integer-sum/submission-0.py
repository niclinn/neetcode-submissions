class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums): 
            if i > 0 and nums[i - 1] == num: 
                continue
            l, r = i + 1, len(nums) - 1
            target = -num
            while l < r: 
                twoSum = nums[l] + nums[r]
                if twoSum > target: 
                    r -= 1
                elif twoSum < target: 
                    l += 1
                else: 
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
        return res