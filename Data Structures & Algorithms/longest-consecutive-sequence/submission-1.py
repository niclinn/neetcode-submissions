class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for num in numsSet: 
            curr = num
            length = 0
            while curr in numsSet: 
                length += 1
                curr += 1
            res = max(res, length)
        return res