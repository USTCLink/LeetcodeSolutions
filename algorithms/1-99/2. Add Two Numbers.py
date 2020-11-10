class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None
        dummyHead = current = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            current.next = ListNode(value%10)
            carry = value // 10
            current = current.next
        return dummyHead.next