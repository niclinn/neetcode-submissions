class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid
            
            # Case A: left side is sorted
            if nums[left] <= nums[mid]: 

                # target is in the left side
                if nums[left] <= target < nums[mid]: 
                    right = mid - 1
                else: 
                    left = mid + 1
            
            # Case B: right side is sorted
            else: 

                # target is in the right side
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1
                else: 
                    right = mid - 1
        return -1