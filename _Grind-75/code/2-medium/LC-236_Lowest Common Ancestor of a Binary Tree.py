# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        iterative
        ref1: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/65236/java-python-iterative-solution
        ref2: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/168798/python-solution
        """

        if root == p or root == q:
            return root

        queue = deque([root])
        parent = {}

        # <1> 모든 노드를 순회하며 parent table 채우기
        while not (p in parent and q in parent):
            u = queue.popleft()

            if u.left:
                parent[u.left] = u
                queue.append(u.left)

            if u.right:
                parent[u.right] = u
                queue.append(u.right)

        # <2> p 부터 root 까지 올라가면서 거치는 노드를 path에 기록
        path = set()
        curr = p
        path.add(curr)
        while curr in parent:
            curr = parent[curr]
            path.add(curr)

        # <3> q 부터 root 까지 올라가면서, p의 path에 속하는 노드를 마주치게 되면 멈추고 현재 노드를 반환
        curr = q
        while not curr in path:
            curr = parent[curr]

        return curr

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        recursive 하게 root 부터 내려가면서 p, q 찾기
        ref: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/152682/python-simple-recursive-solution-with-detailed-explanation
        """

        # <1> root가 p 혹은 q와 동일하거나 None이라면 그대로 return
        if root == p or root == q or root == None:
            return root

        # <2> root의 left와 right에 대해 recursive 하게 p와 q 찾기
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # <3> recur 과정에서 찾은 left와 right의 값에 따라 결과 반환
        # left와 right 각각에 p와 q가 위치한다면, root가 LCA
        if left and right:
            return root
        # left와 right 중 한쪽에만 p와 q가 위치한다면, 위치한 쪽이 LCA
        else:
            return left or right
