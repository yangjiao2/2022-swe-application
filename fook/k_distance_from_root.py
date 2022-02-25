# Description

# Given a binary tree (pointer to the root), a target node anywhere in the tree,
# and an integer value K. Return a list of the values of all the nodes that have
# a distance K from the target node. The order of the list does not matter.

class TreeNode:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

def knodes(root: TreeNode, target: int, k: int):
    if root == None:
        return []

    graph = defaultdict(list)
    dfs(root, graph)

    #bfs
    output = [] # 8 2 6 7
    visited = set([target]) # 3 5 9 4 8 2 6 7 1
    queue = deque([(target, 0)])
    while queue:
        node, depth = queue.popleft()
        if depth == k:
            output.append(node)
        elif depth > k:
            break

        for nei in graph[node]:
            if nei not visited:
                visited.add(nei)
                queue.append((nei, depth + 1))

    return output

# 1: 8
# 3: 5, 9
# 5: 8, 3
# 8: 5, 1
# 9, 3
# ...

def dfs(root, graph):
    if root.left:
        graph[root.val].append(root.left.val)
        graph[root.left.val].append(root.val)
        dfs(root.left)

    if root.right:
        graph[root.val].append(root.right.val)
        graph[root.right.val].append(root.val)
        dfs(root.right)
