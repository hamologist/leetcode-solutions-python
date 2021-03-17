class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, ln: ListNode) -> str:
        if ln.next is None:
            return str(ln.val)
        return str(self.reverse_list(ln.next)) + str(ln.val)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        word = str(int(self.reverse_list(l1)) + int(self.reverse_list(l2)))
        second = ans
        for char in word[:0:-1]:
            second.val = int(char)
            second.next = ListNode()
            second = second.next
        second.val = int(word[0])

        return ans


def print_list(ln: ListNode):
    while ln is not None:
        print(ln.val, end="")
        ln = ln.next
    print()


if __name__ == '__main__':
    solution = Solution()

    _l1 = ListNode(2, ListNode(4, ListNode(3)))
    _l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(solution.reverse_list(_l1))
    print(solution.reverse_list(_l2))
    print_list(solution.addTwoNumbers(_l1, _l2))
    print()

    _l1 = ListNode(0)
    _l2 = ListNode(0)
    print(solution.reverse_list(_l1))
    print(solution.reverse_list(_l2))
    print_list(solution.addTwoNumbers(_l1, _l2))
    print()

    _l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    _l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(solution.reverse_list(_l1))
    print(solution.reverse_list(_l2))
    print_list(solution.addTwoNumbers(_l1, _l2))
    print()
