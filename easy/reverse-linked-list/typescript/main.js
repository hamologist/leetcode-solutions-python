var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
    ListNode.prototype.toArray = function () {
        var head = this;
        var list = [];
        while (head !== null) {
            list.push(head.val);
            head = head.next;
        }
        return list;
    };
    return ListNode;
}());
function reverseList(head) {
    var prev = null;
    while (head !== null) {
        var next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
}
console.log(reverseList(new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))))).toArray());
