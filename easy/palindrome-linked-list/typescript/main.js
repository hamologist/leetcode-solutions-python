var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
    return ListNode;
}());
function isPalindrome(head) {
    var asList = [];
    var evaluation = true;
    while (head !== null) {
        asList.push(head.val);
        head = head.next;
    }
    var length = asList.length;
    for (var i = 0; i < Math.floor(length / 2); i++) {
        if (asList[i] !== asList[length - i - 1]) {
            evaluation = false;
            break;
        }
    }
    return evaluation;
}
console.log(isPalindrome(new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))))));
