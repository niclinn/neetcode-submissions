class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.end = False
    
    def addWord(self, word: str) -> None: 
        curr = self
        for ch in word: 
            if ch not in curr.children: 
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        res, visit = set(), set()

        for word in words: 
            root.addWord(word)

        def dfs(r, c, node, word): 
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visit or board[r][c] not in node.children
                ): 
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end: 
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))
        
        for r in range(ROWS): 
            for c in range(COLS): 
                dfs(r, c, root, "")
        
        return list(res)













