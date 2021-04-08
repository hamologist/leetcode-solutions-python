import { TreeNode } from "../../../_shared/typescript/TreeNode";

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
);
