class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)): 
            temp = temperatures[i]
            wait = 0
            for j in range(i + 1, len(temperatures)): 
                future_temp = temperatures[j]
                if future_temp > temp: 
                    wait = j - i
                    break
            res.append(wait)
        
        return res
        