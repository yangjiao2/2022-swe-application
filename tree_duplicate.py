# 652. Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    def dfs(self, root):
        if not root:
            return " "
        n = str(root.val) + "," + self.dfs(root.left) + "," + self.dfs(root.right)
        if n in self.s and n not in self.counted:
            self.counted[n] = 1
            self.ans.append(root)
            return n
        self.s.add(n)
        return n

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        self.s = set()
        self.ans = []
        self.counted = dict()
        self.dfs(root)
        return self.ans
