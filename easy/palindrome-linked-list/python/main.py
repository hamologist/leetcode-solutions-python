class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        as_list = []
        while head is not None:
            as_list.append(head.val)
            head = head.next

        return as_list == as_list[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
