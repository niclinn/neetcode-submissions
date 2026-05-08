class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        
        freq = {}
        for n in nums: 
            freq[n] = 1 + freq.get(n, 0)
        
        for num, cnt in freq.items(): 
            buckets[cnt].append(num)
        
        res = []
        for bucket in reversed(buckets): 
            for num in bucket: 
                res.append(num)
                if len(res) >= k: 
                    return res
        