class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        temp = slow.next
        slow.next = None
        prev = None
        curr = temp
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge
        while prev and head:
            next1 = head.next
            next2 = prev.next
            head.next = prev
            prev.next = next1
            head = next1
            prev = next2
        