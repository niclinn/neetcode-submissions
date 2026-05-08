class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)

        if len(s) != len(t): 
            return False

        for ch in s: 
            sMap[ch] += 1
        
        for ch in t: 
            sMap[ch] -= 1

            if sMap[ch] < 0: 
                return False

        return True