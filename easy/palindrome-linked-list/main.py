from _shared.linked_list import ListNode, list_to_list_node


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        as_list = []
        while head is not None:
            as_list.append(head.val)
            head = head.next

        return as_list == as_list[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(list_to_list_node([1, 2, 2, 1])))
