#Primera idea:
class ListNode:
    def __init__(self, val=0, next=None):         
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr:
            if curr.val==curr.next.val and curr.next!=None:
                if curr.next.next==None:
                    curr.next=None
                    curr=curr.next
                else:
                    curr.next=curr.next.next
                    curr=curr.next.next
            else:
                curr=curr.next
        return head

#Segunda idea:
class ListNode:
    def __init__(self, val=0, next=None):         
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr:
            if curr.next is not None:
                if curr.next.val==curr.val:
                    curr.next= curr.next.next
                else:
                    curr=curr.next
            else:
                curr=curr.next
        return head