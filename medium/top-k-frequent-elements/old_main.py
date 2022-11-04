import heapq
from collections import Counter
from typing import NamedTuple


class Solution:

    def topKFrequentCounter(self, nums: list[int], k: int) -> list[int]:
        return [count[0] for count in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter: dict[int, int] = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return heapq.nlargest(k, counter.keys(), key=counter.get)

    def topKFrequentWithSortedCount(self, nums: list[int], k: int) -> list[int]:
        counter: dict[int, int] = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return sorted(counter, key=counter.get, reverse=True)[:k]

    def topKFrequentWithNamedTuple(self, nums: list[int], k: int) -> list[int]:
        class TopK(NamedTuple):
            num: int
            count: int

        top_k: list[TopK] = []
        counter: dict[int, int] = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            top_k.append(TopK(num, count))

        top_k.sort(key=lambda entry: entry.count, reverse=True)

        return [k.num for k in top_k[0:k]]

    def topKFrequentLookups(self, nums: list[int], k: int) -> list[int]:
        top_k = []
        counter: dict[int, int] = {}
        k_lookup: dict[int, int] = {}

        for num in nums:
            current_count = counter.get(num, 0)
            counter[num] = current_count + 1

            if current_count == 0:
                top_k.append(num)
                k_lookup[num] = len(top_k) - 1
            else:
                current_position = k_lookup[num]
                move_to = current_position - 1
                while move_to >= 0 and counter[top_k[move_to]] < current_count + 1:
                    top_k[move_to + 1], top_k[move_to] = top_k[move_to], top_k[move_to + 1]
                    k_lookup[top_k[move_to + 1]] = move_to + 1
                    k_lookup[top_k[move_to]] = move_to
                    move_to -= 1

        return top_k[0:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 2))
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(solution.topKFrequent([1], 1))
