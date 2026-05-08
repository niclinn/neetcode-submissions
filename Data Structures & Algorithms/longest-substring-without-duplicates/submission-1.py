class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0
        left = 0

        for i in range(len(s)): 
            ch = s[i]
            while ch in chars: 
                chars.remove(s[left])
                left += 1
            chars.add(ch)
            res = max(res, i - left + 1)
        return res