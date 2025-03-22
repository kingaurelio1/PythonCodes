class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.list1=[]
    def get_list(self):
        if head is None:
            return []
        else:
            while head is not None:
                self.list1.append(head)
                head=head.next
            return self.list1

def reverse(head):
    for i in head