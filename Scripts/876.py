# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         record = {}
#         idx = 0
#         while head:
#             record[idx] = head
#             idx += 1
#             head = head.next
        
#         return record[math.floor(idx/2)]
            
        
        ans = head
        idx = 0
        while head:
            if idx % 2:
                ans = ans.next
            idx += 1
            head = head.next
            
        return ans  