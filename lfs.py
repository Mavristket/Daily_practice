from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def left_view(root):

    if root is None:
        return []

    q = deque([root])
    result = []

    while q:
        n = len(q)

        for i in range(n):
            node = q.popleft()

            if i == 0:           # first node of level
                result.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    return result