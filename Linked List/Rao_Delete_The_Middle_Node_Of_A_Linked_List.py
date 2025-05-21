class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return dummy.next