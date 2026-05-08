class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s: 
            if ch not in mapping: 
                stack.append(ch)
            else: 
                if not stack or mapping[ch] != stack.pop(): 
                    return False
        return True if not stack else False