class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(cost) - 1, -1, -1): 
            curr = cost[i] + min(one, two)
            one, two = curr, one
        return min(one, two)