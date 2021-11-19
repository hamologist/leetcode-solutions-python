from collections import deque
from typing import Deque, List, Optional

from _shared.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack: Deque[TreeNode] = deque()
        inorder = []

        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current.val)
            current = current.right

        return inorder

    def inorderTraversalWithTwoStacks(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack: Deque[TreeNode] = deque([root])
        left_stack: Deque[TreeNode] = deque()
        inorder = []

        while stack or left_stack:
            if stack:
                current = stack.pop()
                if current.left:
                    stack.append(current.left)
                left_stack.append(current)
            elif left_stack:
                current = left_stack.pop()
                inorder.append(current.val)
                if current.right:
                    stack.append(current.right)

        return inorder

    def inorderTraversalWithRecursion(self, root: Optional[TreeNode]) -> List[int]:
        memo = []

        def inner(_root: Optional[TreeNode]):
            if _root is None:
                return

            inner(_root.left)
            memo.append(_root.val)
            inner(_root.right)

        inner(root)
        return memo


if __name__ == '__main__':
    solution = Solution()
    print(solution.inorderTraversal(
        TreeNode(
            1,
            None,
            TreeNode(
                2,
                TreeNode(3)
            )
        ))
    )
    print(solution.inorderTraversal(None))
    print(solution.inorderTraversal(TreeNode(1)))
    print(solution.inorderTraversal(
        TreeNode(
            1,
            TreeNode(2)
        ))
    )
    print(solution.inorderTraversal(
        TreeNode(
            1,
            None,
            TreeNode(2)
        ))
    )
