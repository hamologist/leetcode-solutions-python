class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        white = set(range(0, numCourses))
        grey = set()
        black = set()
        nodes: dict[int, list[int]] = {index: [] for index in range(0, numCourses)}
        for prerequisite in prerequisites:
            nodes[prerequisite[0]].append(prerequisite[1])

        def has_cycle(_node: int) -> bool:
            if _node in black:
                return False
            if _node in grey:
                return True

            white.remove(_node)
            grey.add(_node)
            for require in nodes[_node]:
                if has_cycle(require):
                    return True

            grey.remove(_node)
            black.add(_node)
            return False

        while white:
            if has_cycle(next(iter(white))):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
