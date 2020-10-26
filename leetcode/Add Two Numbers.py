class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def addTwoNumbers(l1:ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry=0
    while l1 or l2 or carry:
        sum=0
        if l1:
            sum+=l1.val
            l1=l1.next
        if l2:
            sum+=l2.val
            l2=l2.next

        carry, val=divmod(sum+carry, 10)
        root.next=ListNode(val)
        root=root.next

    return head.next

a=ListNode(1)
b=ListNode(8)
#c=ListNode(3)
a.next=b
#b.next=c

d=ListNode(0)
#e=ListNode(6)
#f=ListNode(4)
#d.next=e
#e.next=f

ans=addTwoNumbers(a, d)

while ans!=None:
    print(ans.val)
    ans=ans.next
