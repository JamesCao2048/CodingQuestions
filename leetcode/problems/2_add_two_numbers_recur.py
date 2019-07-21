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
        self.addhHelper(l1, l2, lr, 0)
        return lr

# 时间及空间效率与迭代版本类似，可能因为Python自动做了尾递归优化
    def addhHelper(self, l1, l2, lr, p):
        if not l1 and not l2:
            return
        if not l1:
            lr.val = l2.val + p
            if l2.next or lr.val > 9:
                lr.next = ListNode(lr.val // 10)
                self.addhHelper(l1, l2.next, lr.next, lr.val // 10)
                lr.val %= 10
            return
        if not l2:
            lr.val = l1.val + p
            if l1.next or lr.val > 9:
                lr.next = ListNode(lr.val // 10)
                self.addhHelper(l1.next, l2, lr.next, lr.val // 10)
                lr.val %= 10
            return
        lr.val = l1.val + l2.val + p

        if l1.next or l2.next or lr.val > 9:
            lr.next = ListNode(lr.val // 10)
            self.addhHelper(l1.next, l2.next, lr.next, lr.val // 10)
            lr.val %= 10
        return
