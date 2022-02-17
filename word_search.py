# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/
# solution: https://leetcode.com/problems/word-search-ii/discuss/1748107/Python-Backtracking-%2B-Trie-or-Animated-GIF

class Node:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):  # - time:  O(W)  , space: O(W)
        root = self.root
        for ch in word:
            if ch not in root.child:
                root.child[ch] = Node(ch)
            root = root.child[ch]
        root.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # -- helper --
        def dfs(root, path, x, y):

            if self.numWords == 0:
                return

            if root.end:
                res.add(path)
                self.numWords -= 1
                root.end = False

            if x > len(grid) - 1 or x < 0 or y > len(grid[0]) - 1 or y < 0:
                return

            char = grid[x][y]
            if char not in root.child:
                return

            if grid[x][y] == "#":
                return

            grid[x][y] = "#"
            dfs(root.child[char], path + char, x + 1, y)
            dfs(root.child[char], path + char, x, y + 1)
            dfs(root.child[char], path + char, x - 1, y)
            dfs(root.child[char], path + char, x, y - 1)
            grid[x][y] = char

        # -- main --

        # -- build the trie -- time: O(numWords)*O(W) = O(W*numWords) , space: (W*numWords)
        trie = Trie()
        root = trie.root
        for word in words:
            trie.insert(word)

        # scan the grid
        # backtracking DFS (just like the MED version of this question)
        # instead of an indx for a word - we pass the root of the trie
        # dfs() is how we build the path

        # -- scan each cell and invoke a dfs
        grid = board
        res = set()
        self.numWords = len(words)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                dfs(root, "", x, y)
        return res

# thinking process:
# - trie + dfs : Time = (N*M)*3^W
# - search element with order = prefix search
# - build trie with attribute: children (dict) and end (bool)
# - mark path (visited cell)
