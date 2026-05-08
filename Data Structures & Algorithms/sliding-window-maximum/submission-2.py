class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = collections.deque()
        l = r = 0

        while r < len(nums): 

            # 1. maintain monotonic decreasing queue
            while queue and nums[queue[-1]] < nums[r]: 
                queue.pop()
            queue.append(r)

            # 2. remove tail of window
            if l > queue[0]: 
                queue.popleft()
            
            # 3. only update output when window is the right size
            if (r + 1) >= k: 
                output.append(nums[queue[0]])
                l += 1
            r += 1
        return output