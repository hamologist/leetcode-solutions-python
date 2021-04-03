class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }

    toArray(): Array<number> {
      let head: ListNode | null = this;
      let list: Array<number> = [];
      while (head !== null) {
        list.push(head.val);
        head = head.next;
      }

      return list;
    }
}

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
    new ListNode(1,
      new ListNode(2,
        new ListNode(3,
          new ListNode(4,
            new ListNode(5)
          )
        )
      )
    )
  ).toArray()
)
