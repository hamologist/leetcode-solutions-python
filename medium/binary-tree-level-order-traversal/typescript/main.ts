import { TreeNode } from "../../../_shared/typescript/TreeNode";

function levelOrder(root: TreeNode | null): number[][] {
  const nums = new Array<Array<number>>();

  (function inner(node: TreeNode | null, level: number) {
    if (node === null) {
      return;
    }
    if (level >= nums.length) {
      nums.push([node.val]);
    } else {
      nums[level].push(node.val)
    }

    inner(node.left, level + 1);
    inner(node.right, level + 1);
  })(root, 0);

  return nums;
}

console.log(
  levelOrder(
    new TreeNode(3,
      new TreeNode(9),
      new TreeNode(20,
        new TreeNode(15),
        new TreeNode(7),
      ),
    )
  )
)