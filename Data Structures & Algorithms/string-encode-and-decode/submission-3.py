class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs: 
            code += str(len(s)) + '/' + s
        return code 

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []

        while i < len(s): 
            while s[i] != '/': 
                i += 1
            size = int(s[j:i])
            res.append(s[i + 1: i + size + 1])
            i, j = i + size + 1, i + size + 1

        return res
        