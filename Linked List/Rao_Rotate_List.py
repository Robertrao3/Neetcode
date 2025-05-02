# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        
        curr = head
        length = 1

        while curr.next:
            curr = curr.next
            length += 1
        
        k %= length

        if k == 0:
            return head
        
        curr.next = head
        curr = head

        for i in range(1, length - k):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head