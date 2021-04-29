from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val: int = val
        self.next: Optional['ListNode'] = next_node

    def to_list(self) -> List[int]:
        head = self
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next

        return output


def list_to_list_node(nums: List[int]) -> Optional[ListNode]:
    current = None
    next_node = None
    for i in range(len(nums) - 1, -1, -1):
        current = ListNode(nums[i])
        current.next = next_node
        next_node = current

    return current
