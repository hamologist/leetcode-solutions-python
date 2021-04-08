import { inOrder, TreeNode } from "../../../_shared/typescript/TreeNode";

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

console.log(inOrder(sortedArrayToBST([-10, -3, 0, 5, 9])));
console.log(inOrder(sortedArrayToBST([1, 3])));
