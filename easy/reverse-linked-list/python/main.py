from _shared.python.linked_list import ListNode, list_to_list_node


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


if __name__ == '__main__':
    solution = Solution()
    _input = list_to_list_node([1, 2, 3, 4, 5])
    print(solution.reverseList(_input).to_list())
