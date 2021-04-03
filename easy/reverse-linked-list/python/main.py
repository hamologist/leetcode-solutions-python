from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = head

        if head is not None:
            head = head.next
            prev.next = None
        while head is not None:
            _next = head.next
            head.next = prev
            prev = head
            head = _next

        return prev


def list_node_to_list(head: ListNode) -> List[int]:
    _return = []
    while head is not None:
        _return.append(head.val)
        head = head.next

    return _return


if __name__ == '__main__':
    solution = Solution()
    _input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(list_node_to_list(solution.reverseList(_input)))
