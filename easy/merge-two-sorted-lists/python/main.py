from typing import Optional

from _shared.python.linked_list import ListNode, list_to_list_node
from _shared.python.test import BaseTest


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoListsWithIteration(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        current = head
        while l1 or l2:
            if l1 is None:
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next

        return head


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            [1, 1, 2, 3, 4, 4],
            self.solution.mergeTwoLists(
                list_to_list_node([1, 2, 4]),
                list_to_list_node([1, 3, 4])
            ).to_list()
        )

    def test_two(self):
        self.assertEqual(
            None,
            self.solution.mergeTwoLists(None, None)
        )

    def test_three(self):
        self.assertEqual(
            [0],
            self.solution.mergeTwoLists(
                None,
                list_to_list_node([0])
            ).to_list()
        )


if __name__ == '__main__':
    Test.execute()
