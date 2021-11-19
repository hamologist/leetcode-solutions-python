from typing import Optional

from _shared.linked_list import ListNode, list_to_list_node
from _shared.test import BaseTest


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head

        return head

    def oddEvenListIterativeInPlace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = False
        latest_odd = head
        latest_even = head.next
        first_even = latest_even
        current = head.next
        while current:
            if odd:
                latest_odd.next = current
                latest_even.next = current.next
                current.next = first_even
                latest_odd = current
                current = latest_even.next
            else:
                latest_even = current
                current = current.next
            odd = not odd

        return head


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            [1, 3, 5, 2, 4],
            self.solution.oddEvenList(list_to_list_node([1, 2, 3, 4, 5])).to_list()
        )

    def test_two(self):
        self.assertEqual(
            [2, 3, 6, 7, 1, 5, 4],
            self.solution.oddEvenList(list_to_list_node([2, 1, 3, 5, 6, 4, 7])).to_list()
        )


if __name__ == '__main__':
    Test.execute()
