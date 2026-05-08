class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        # iterate through the bars
        for i, h in enumerate(heights): 
            start = i # assume that the area can't extend left

            # stack[-1][1] -> nearest bar's to the left's height
            # (on top of the stack)
            # check if that is greater than current height, 
            # then we can extend our rectangle
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()

                # compare current max vs area given from calc
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea