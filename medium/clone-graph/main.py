from copy import deepcopy
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return deepcopy(node)

    def cloneGraphWithRecursion(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        memo: dict[int, 'Node'] = {}

        def _inner(_node: 'Node') -> 'Node':
            new_node = Node(_node.val)
            memo[_node.val] = new_node

            for neighbor in _node.neighbors:
                if neighbor.val in memo:
                    new_node.neighbors.append(memo[neighbor.val])
                else:
                    new_node.neighbors.append(_inner(neighbor))

            return new_node

        return _inner(node)


if __name__ == '__main__':
    solution = Solution()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)

    one.neighbors = [two, four]
    two.neighbors = [one, three]
    three.neighbors = [two, four]
    four.neighbors = [one, three]
    solution.cloneGraph(one)
