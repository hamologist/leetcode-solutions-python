class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function inorderTraversal(root: TreeNode | null): number[] {
  const vals: Array<number> = [];
  function inner(root: TreeNode | null): void {
    if (root == null) {
      return;
    }
    if (root.left === null && root.right === null) {
      vals.push(root.val);
      return;
    }

    inner(root.left);
    vals.push(root.val);
    inner(root.right);
  }

  inner(root);
  return vals;
}

console.log(
  inorderTraversal(
    new TreeNode(1,
      null,
      new TreeNode(2,
        new TreeNode(3),
        null
      ))
  )
)
