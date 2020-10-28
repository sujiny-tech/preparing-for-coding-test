# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur=root=ListNode(0)
        
        while head:
            while cur.next and cur.next.val<head.val:
                cur=cur.next
            #head>cur.next.val
            cur.next, head.next, head=head, cur.next, head.next
            
            if head and cur.val>head.val:
                cur=root
        return root.next
