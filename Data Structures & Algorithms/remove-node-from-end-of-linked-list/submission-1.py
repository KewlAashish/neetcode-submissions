
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        size = 0
        temp = head

        while temp:
            size += 1
            temp = temp.next

        prev = dummy

        for _ in range(size - n):
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
