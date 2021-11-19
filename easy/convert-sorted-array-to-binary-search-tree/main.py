from typing import List, Optional

from _shared.tree_node import TreeNode, inorder_traversal


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def _inner(_nums: List[int]) -> Optional[TreeNode]:
            _mid = int(len(_nums) / 2)
            _left = _nums[0:_mid]
            _right = _nums[_mid + 1:]
            return TreeNode(
                _nums[_mid],
                _inner(_left) if len(_left) else None,
                _inner(_right) if len(_right) else None,
            )

        return _inner(nums)


if __name__ == '__main__':
    solution = Solution()
    print(inorder_traversal(solution.sortedArrayToBST([-10, -3, 0, 5, 9])))
    print(inorder_traversal(solution.sortedArrayToBST([1, 3])))
