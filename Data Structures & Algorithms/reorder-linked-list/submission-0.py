# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        nodes_list = []
        while temp:
            nodes_list.append(temp)
            temp = temp.next

        n = len(nodes_list)
        left = 0
        right = n - 1

        while left < right:
            nodes_list[left].next = nodes_list[right]
            left += 1

            if left == right:
                break

            nodes_list[right].next = nodes_list[left]
            right -= 1

        if nodes_list:
            nodes_list[left].next = None

        return