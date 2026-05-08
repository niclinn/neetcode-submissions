class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max_count = 0

        for num in numsSet: 
            curr_num, count = num, 1
            
            while curr_num + 1 in numsSet: 
                count += 1
                curr_num += 1
            max_count = max(max_count, count)
        
        return max_count
            