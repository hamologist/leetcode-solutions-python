from collections import deque
from typing import List, Optional

from _shared.python.test import BaseTest
from _shared.python.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans: List[List[int]] = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node: TreeNode
            level: int
            node, level = queue.popleft()

            if node is None:
                continue

            if len(ans) == level:
                ans.append([node.val])
            else:
                ans[level].append(node.val)

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return ans

    def levelOrderWithRecurrsion(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans: List[List[int]] = []

        def _inner(_root: Optional[TreeNode], level: int):
            if _root is None:
                return

            if len(ans) == level:
                ans.append([_root.val])
            else:
                ans[level].append(_root.val)

            _inner(_root.left, level + 1)
            _inner(_root.right, level + 1)

        _inner(root, 0)
        return ans


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            [[3], [9, 20], [15, 7]],
            self.solution.levelOrder(
                TreeNode(
                    3,
                    TreeNode(9),
                    TreeNode(
                        20,
                        TreeNode(15),
                        TreeNode(7)
                    )
                )
            )
        )

    def test_two(self):
        self.assertEqual(
            [[1]],
            self.solution.levelOrder(
                TreeNode(1)
            )
        )

    def test_three(self):
        self.assertEqual(
            [],
            self.solution.levelOrder(None)
        )


if __name__ == '__main__':
    Test.execute()
