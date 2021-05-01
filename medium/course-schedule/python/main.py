class Node:
    requires: list['Node']

    def __init__(self, val=0):
        self.val = val
        self.requires = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        white = set(range(0, numCourses))
        grey = set()
        black = set()
        nodes: dict[int, Node] = {index: Node(index) for index in range(0, numCourses)}
        for prerequisite in prerequisites:
            nodes[prerequisite[0]].requires.append(nodes[prerequisite[1]])

        def has_cycle(_node: Node) -> bool:
            if _node.val in black:
                return False
            if _node.val in grey:
                return True

            white.remove(_node.val)
            grey.add(_node.val)
            for neighbor in _node.requires:
                if has_cycle(neighbor):
                    return True

            grey.remove(_node.val)
            black.add(_node.val)
            return False

        while white:
            if has_cycle(nodes[next(iter(white))]):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
