# Add Two Numbers
# Medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lr = ListNode(0)
        lc = lr
        p = 0
        while l1 and l2:
            lc.val = l1.val + l2. val + p
            p = lc.val // 10
            lc.val %= 10
            if l1.next or l2.next or p:
                lc.next = ListNode(p)
                lc = lc.next
            l1 = l1.next
            l2 = l2.next
        l_t = l1 if l1 else l2
        while l_t:
            lc.val = l_t.val + p
            p = lc.val // 10
            lc.val %= 10
            if l_t.next or p:
                lc.next = LisNode(p)
                lc = lc.next
            l_t = l_t.next

        return lr
