export class ListNode {
  val: number
  next: ListNode | null

  constructor(val?: number, next?: ListNode | null) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
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

export function arrayToListNode(nums: number[]): ListNode | null {
  let current: ListNode | null = null;
  let next: ListNode | null = null;
  for (let i = nums.length - 1; i >= 0; i--) {
    current = new ListNode(nums[i]);
    current.next = next;
    next = current;
  }

  return current;
}

