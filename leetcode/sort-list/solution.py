# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head 
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
            
        return self.mergeSort(head, n)
        
    def mergeSort(self, node, length):
        if length == 1: return node
        mid = length // 2
        left_node = node
        left = self.mergeSort(left_node, mid)
        right_node = node
        for i in range(mid):
            right_node = right_node.next
        
        right = self.mergeSort(right_node, length - mid)
        return self.merge(left, right, mid, length - mid)
    
    def merge(self, left, right, left_size, right_size):
        dummy = ListNode()
        res = dummy
        while left_size > 0 and right_size > 0:
            if left.val < right.val:
                res.next = ListNode(left.val)
                left = left.next
                left_size -= 1
            else:
                res.next = ListNode(right.val)
                right = right.next
                right_size -= 1
            res = res.next
            
        if left_size == 0:
            while right_size > 0:
                res.next = ListNode(right.val)
                right = right.next
                res = res.next
                right_size -= 1
        elif right_size == 0:
            while left_size > 0:
                res.next = ListNode(left.val)
                left = left.next
                res = res.next
                left_size -= 1
            
        return dummy.next
        