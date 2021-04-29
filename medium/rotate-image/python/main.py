from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for y in range(0, len(matrix)):
            for x in range(0, y):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        for y in range(0, len(matrix)):
            matrix[y] = matrix[y][::-1]


if __name__ == '__main__':
    solution = Solution()
    _input = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    solution.rotate(_input)
    print(_input)

    _input = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    solution.rotate(_input)
    print(_input)
