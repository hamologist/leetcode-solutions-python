// @ts-ignore
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

function kthSmallest(root: TreeNode, k: number): number {
    let val: number = root.val;
    let kCount: number = 0;

    (function inner(root: TreeNode | null): void {
        if (root === null) {
            return;
        }

        if (kCount < k) {
            inner(root.left);
        }

        if (kCount < k) {
            val = root.val;
            kCount += 1;
        }

        if (kCount < k) {
            inner(root.right);
        }
    })(root);

    return val;
}

console.log(
  kthSmallest(
    new TreeNode(3,
      new TreeNode(1,
        null,
        new TreeNode(2)
      ),
      new TreeNode(4)
    ), 1
  )
)

console.log(
  kthSmallest(
    new TreeNode(5,
      new TreeNode(3,
        new TreeNode(2,
          new TreeNode(1)
        ),
        new TreeNode(4)
      ),
      new TreeNode(6)
    ), 3
  )
)
