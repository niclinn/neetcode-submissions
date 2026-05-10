class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        res = 0
        for n in mp: 
            temp = n
            seqLen = 0
            while temp in mp: 
                seqLen += 1
                temp -= 1
            res = max(res, seqLen)
        return res