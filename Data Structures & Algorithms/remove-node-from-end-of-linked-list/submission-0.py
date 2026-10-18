# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(0)
        prev = new_head
        curr = head
        count = 0

        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next

        while curr:
            if count == size - n:
                prev.next = curr.next
                break
            else:
                if prev == new_head:
                    new_head.next = curr

                prev = curr
                curr = curr.next
            
            count += 1
        
        return new_head.next