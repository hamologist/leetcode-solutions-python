from _shared.linked_list import ListNode, list_to_list_node


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution()

    _input = list_to_list_node([4, 5, 1, 9])
    solution.deleteNode(_input.next)
    print(_input.next.val)
