# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, l1, l2):
        new_head = ListNode(0)
        temp = new_head

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return new_head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge2Lists(l1, l2))

            lists = merged_lists

        return lists[0]
