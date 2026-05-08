class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs: 
            code += str(len(s)) + '/' + s
        return code 

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s): 
            j = i
            while s[i] != '/': 
                i += 1
            res.append(s[i+1:i + int(s[j:i]) + 1])
            i = i + int(s[j:i]) + 1
        return res
        