class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = [0] * (ord('z') - ord('a') + 1)
        listT = [0] * (ord('z') - ord('a') + 1)

        for ch in s: 
            listS[ord(ch) - ord('a')] += 1
        
        for ch in t: 
            listT[ord(ch) - ord('a')] += 1
        
        return listS == listT
