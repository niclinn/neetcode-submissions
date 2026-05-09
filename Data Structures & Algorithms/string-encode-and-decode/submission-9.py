class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += str(len(s)) + '/' + s
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < len(s): 
            while s[r] != '/': 
                r += 1
            strLen = int(s[l:r])
            res.append(s[r + 1: r + 1 + strLen])
            l = r = r + 1 + strLen
        return res

                