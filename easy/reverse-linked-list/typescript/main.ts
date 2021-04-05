import { arrayToListNode, ListNode } from "../../../_shared/typescript/LinkedList";

function reverseList(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;
  while (head !== null) {
    let next: ListNode | null = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }

  return prev;
}

console.log(
  reverseList(
    arrayToListNode([1, 2, 3, 4, 5])
  )?.toArray()
)