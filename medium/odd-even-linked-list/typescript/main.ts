import { arrayToListNode, ListNode } from "../../../_shared/typescript/LinkedList";

function oddEvenList(head: ListNode | null): ListNode | null {
  if (head === null || head.next === null || head.next.next === null) {
    return head
  }

  let oddPtr = head;
  let evenPtr = head.next;
  const evenPtrHead = evenPtr;
  let oddTarget = evenPtr.next;
  let evenTarget = oddTarget?.next || null;
  while (oddTarget !== null) {
    oddPtr.next = oddTarget;
    oddTarget.next = evenTarget;
    evenPtr.next = evenTarget;

    if (evenTarget === null || evenTarget.next === null) {
      oddTarget.next = evenPtrHead;
      return head;
    }
    oddPtr = oddTarget;
    evenPtr = evenTarget;
    oddTarget = evenPtr.next
    evenTarget = oddTarget?.next || null;
  }

  return head;
}

console.log(
  oddEvenList(
    arrayToListNode([1, 2, 3, 4, 5])
  )?.toArray()
)

console.log(
  oddEvenList(
    arrayToListNode([2, 1, 3, 5, 6, 4, 7])
  )?.toArray()
)