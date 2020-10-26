class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def isPalindrome(head:ListNode) -> bool:
    isTrue=True
    list_=[]
    while head!=None:
        list_.append(head.val)
        head=head.next
    print(list_)
    left, right=0, len(list_)-1
    while left<right:
        if list_[left]==list_[right]:
            left+=1
            right-=1
        else:
            isTrue=False
            break
    return isTrue

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next=b
b.next=c
ans=isPalindrome(a)
print(ans)