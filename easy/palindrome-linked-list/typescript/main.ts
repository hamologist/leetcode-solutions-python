import { arrayToListNode, ListNode } from "../../../_shared/typescript/LinkedList";

function isPalindrome(head: ListNode | null): boolean {
  let asList: Array<number> = [];
  let evaluation: boolean = true;
  while (head !== null) {
    asList.push(head.val)
    head = head.next
  }

  const length = asList.length;
  for (let i = 0; i < Math.floor(length / 2); i++) {
    if (asList[i] !== asList[length - i - 1]) {
      evaluation = false;
      break;
    }
  }

  return evaluation;
}

console.log(
  isPalindrome(
    arrayToListNode([1, 2, 2, 1])
  )
)