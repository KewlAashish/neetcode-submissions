# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, k):
        new_head = None
        next_ptr = None

        prev = None
        curr = head
        count = 0

        while count < k:
            # if count == k - 1:
            #     next_ptr = curr.next

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
            count += 1

        return prev, curr
            

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp = head
        size = 0

        while temp:
            size += 1
            temp = temp.next

        curr_node = head
        dummy_head = ListNode(-1)
        temp = dummy_head
        count = 0

        while count + k <= size:
            new_head, next_curr_node = self.reverse(curr_node, k)
            temp.next = new_head
            temp = curr_node
            curr_node = next_curr_node
            count += k

        if curr_node:
            temp.next = curr_node

        return dummy_head.next

