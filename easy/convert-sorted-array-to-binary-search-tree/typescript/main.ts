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

function sortedArrayToBST(nums: number[]): TreeNode {
    return (function inner(nums: number[]): TreeNode | null {
        const middle = Math.floor(nums.length / 2);
        const left = nums.slice(0, middle);
        const right = nums.slice(middle + 1);
        return new TreeNode(
          nums[middle],
          left.length > 0 ? inner(nums.slice(0, middle)) : null,
          right.length > 0 ? inner(nums.slice(middle+1)) : null,
        )
    })(nums) || new TreeNode();
}

function inOrder(head: TreeNode) {
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

console.log(inOrder(sortedArrayToBST([-10, -3, 0, 5, 9])));
console.log(inOrder(sortedArrayToBST([1, 3])));
