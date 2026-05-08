class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        def dfs(curr):
            nonlocal res
            if curr == n: 
                res += 1
                return
            if curr > n: 
                return
            
            dfs(curr + 1)
            dfs(curr + 2)
        
        dfs(0)
        return res