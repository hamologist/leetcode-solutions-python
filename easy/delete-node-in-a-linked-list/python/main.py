from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution()

    _head = ListNode(4)
    _current = _head
    for _node in [ListNode(5), ListNode(1), ListNode(9)]:
        _current.next = _node
        _current = _node
    solution.deleteNode(_head.next)
    print(_head.next.val)
