class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_val = "0b"

        while head:
            bin_val += str(head.val)
            head = head.next

        return int(bin_val, 2)

param_3=ListNode(1)
param_2=ListNode(0, param_3)
param_1=ListNode(1, param_2)

res=Solution().getDecimalValue(param_1)
