from _shared.python.linked_list import ListNode, list_to_list_node


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


if __name__ == '__main__':
    solution = Solution()

    _l1 = list_to_list_node([2, 4, 3])
    _l2 = list_to_list_node([5, 6, 4])
    print(solution.reverse_list(_l1))
    print(solution.reverse_list(_l2))
    print("".join([str(num) for num in solution.addTwoNumbers(_l1, _l2).to_list()]))
    print()

    _l1 = list_to_list_node([0])
    _l2 = list_to_list_node([0])
    print(solution.reverse_list(_l1))
    print(solution.reverse_list(_l2))
    print("".join([str(num) for num in solution.addTwoNumbers(_l1, _l2).to_list()]))
    print()

    _l1 = list_to_list_node([9, 9, 9, 9, 9, 9, 9])
    _l2 = list_to_list_node([9, 9, 9, 9])
    print(solution.reverse_list(_l1))
    print(solution.reverse_list(_l2))
    print("".join([str(num) for num in solution.addTwoNumbers(_l1, _l2).to_list()]))
