class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

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
    new ListNode(1,
      new ListNode(2,
        new ListNode(2,
          new ListNode(1)
        )
      )
    )
  )
)