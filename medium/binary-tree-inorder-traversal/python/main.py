from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
