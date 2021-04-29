from typing import Optional

from _shared.python.tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        ans = 0

        def _inner(_root: Optional[TreeNode]):
            nonlocal count, ans, k
            if _root is None or count == k:
                return

            _inner(_root.left)
            if count < k:
                count += 1
                ans = _root.val
            _inner(_root.right)

        _inner(root)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.kthSmallest(
            TreeNode(
                3,
                TreeNode(
                    1,
                    None,
                    TreeNode(2)
                ),
                TreeNode(4)
            ), 1)
    )

    print(
        solution.kthSmallest(
            TreeNode(
                5,
                TreeNode(
                    3,
                    TreeNode(
                        2,
                        TreeNode(1)
                    ),
                    TreeNode(4)
                ),
                TreeNode(6)
            ), 3)
    )
