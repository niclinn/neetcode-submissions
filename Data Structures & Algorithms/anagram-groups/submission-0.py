class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())