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
  if (nums.length === 0) {
    return null;
  }

  return new ListNode(nums[0], arrayToListNode(nums.slice(1)));
}

