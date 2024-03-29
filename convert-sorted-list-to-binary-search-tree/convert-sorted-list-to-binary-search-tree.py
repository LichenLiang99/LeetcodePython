# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
        
#         if not head:
#             return None
        
#         mid = self.findmid(head)
#         root = TreeNode(mid.val)
        
#         #when only 1 value left
#         if head == mid:
#             return root
        
#         root.left = self.sortedListToBST(head)
#         root.right = self.sortedListToBST(mid.next)
#         return root
        
#     def findmid(self, head):
#             prev = None
#             slow = head
#             fast = head

#             while fast and fast.next:
#                 prev = slow
#                 slow = slow.next
#                 fast = fast.next.next
            
#             if prev:
#                 prev.next = None
                
#             return slow

#Inorder Simulation
class Solution:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)   
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)
