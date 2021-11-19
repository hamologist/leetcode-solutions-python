from typing import List, Optional


class TreeNode:

    def __init__(self,
                 val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val: int = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    memo = []

    def inner(_root: Optional[TreeNode]):
        if _root is None:
            return

        inner(_root.left)
        memo.append(_root.val)
        inner(_root.right)

    inner(root)
    return memo
