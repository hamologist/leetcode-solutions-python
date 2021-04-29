from typing import Optional

from _shared.python.linked_list import ListNode, list_to_list_node


class Solution:
    def revised(self, head: Optional[ListNode], val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next

        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> ListNode:
        prev = None
        current = head
        while current is not None:
            next_node = current.next

            if current.val == val:
                if next_node is not None:
                    current.val = next_node.val
                    current.next = next_node.next
                else:
                    if prev is not None:
                        prev.next = None
                        current = prev
                    else:
                        head = None
                        current = head
            else:
                prev = current
                current = current.next

        return head


if __name__ == '__main__':
    solution = Solution()

    _input = list_to_list_node([1, 2, 6, 3, 4, 5, 6])
    print(solution.removeElements(_input, 6).to_list())

    print(solution.removeElements(None, 1))

    _input = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    print(solution.removeElements(_input, 7))
