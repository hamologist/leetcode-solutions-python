from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


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


def linked_list_to_list(node: ListNode):
    _return = []

    while node is not None:
        _return.append(node.val)
        node = node.next

    return _return


if __name__ == '__main__':
    solution = Solution()

    _input = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(linked_list_to_list(solution.removeElements(_input, 6)))

    print(linked_list_to_list(solution.removeElements(None, 1)))

    _input = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    print(linked_list_to_list(solution.removeElements(_input, 7)))
