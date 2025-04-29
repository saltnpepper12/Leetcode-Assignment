# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root: return []
        q, ll = deque([root]), []
        while q:
            rv = None
            for _ in range(len(q)):
                rv = q.popleft()
                if rv.left: q.append(rv.left)
                if rv.right: q.append(rv.right)
            ll.append(rv.val)
        return ll
        
