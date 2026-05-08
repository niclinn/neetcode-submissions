class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. Tortoise and Hare
        slow, fast = 0, 0
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        # 2. Find the duplicate
        slow2 = 0
        while slow != slow2: 
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2