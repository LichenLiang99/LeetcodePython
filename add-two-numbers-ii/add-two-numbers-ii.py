# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        #reverse the 2 lists
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        #reverse it back
        dummy = self.reverse(dummy.next) 
        return dummy    
    
    def reverse(self, head):
        curr = head
        prev = None
        
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev
    
    #time o(n) space o(1) concept linked list, reverse, math