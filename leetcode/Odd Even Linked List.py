class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=None

def oddEvenList(head: ListNode) -> ListNode:
    odd_list=head
    even_list=head.next
    even_head=head.next

    while even_list and even_list.next:
        odd_list.next=odd_list.next.next
        odd_list=odd_list.next

        even_list.next=even_list.next.next
        even_list=even_list.next
    odd_list.next=even_head
    return head

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)
a.next=b
b.next=c
c.next=d
d.next=e

head=oddEvenList(a)
while head!=None:
    print(head.val)
    head=head.next
