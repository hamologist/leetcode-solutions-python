export class TreeNode {
  val: number
  left: TreeNode | null
  right: TreeNode | null
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
  }
}

export function inOrder(head: TreeNode) {
  const vals: number[] = [];

  (function inner(head: TreeNode | null) {
    if (head === null) {
      return;
    }

    inner(head.left);
    vals.push(head.val);
    inner(head.right);
  })(head)

  return vals;
}

