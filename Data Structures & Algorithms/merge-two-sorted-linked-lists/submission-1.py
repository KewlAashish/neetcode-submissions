# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2

        new_head = None
        temp = ListNode(0)

        while temp1 or temp2:
            if not temp1:
                temp.next = temp2
                if not new_head:
                    new_head = temp2
                break
            
            if not temp2:
                temp.next = temp1
                if not new_head:
                    new_head = temp1
                break

            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            
            temp = temp.next

            if not new_head:
                new_head = temp

        return new_head