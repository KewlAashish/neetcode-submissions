# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1_list: Optional[ListNode], l2_list: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1 = [3, 2, 1]
        l2 = [6, 5, 4]

        if len(l1) < len(l2):
            l1, l2 = l2, l1

        n = len(l1)
        m = len(l2)

        ans = []
        curr = 0
        carry = 0

        while carry or i < n
            n1 = 0 if i > n else l1[i]
            n2 = 0 if i > m else l2[i]

            ans.append(n1 + n2 + carry)
            carry = ans[curr] % 10

        ans = ans[::-1]

        dummy = ListNode(0)
        temp = dummy
        for i in ans:
            temp.next = ListNode(i)
            temp = temp.next

        return dummy.next
        """
        l1 = []
        l2 = []
        temp = l1_list
        while temp:
            l1.append(temp.val)
            temp = temp.next
        
        temp = l2_list
        while temp:
            l2.append(temp.val)
            temp = temp.next

        if len(l1) < len(l2):
            l1, l2 = l2, l1

        n = len(l1)
        m = len(l2)

        ans = []
        carry = 0
        i = 0

        while carry or i < n:
            n1 = 0 if i >= n else l1[i]
            n2 = 0 if i >= m else l2[i]
            curr_sum = n1 + n2 + carry

            ans.append(curr_sum % 10)
            carry = curr_sum // 10
            i += 1

        # ans = ans[::-1]

        dummy = ListNode(0)
        temp = dummy
        for i in ans:
            temp.next = ListNode(i)
            temp = temp.next

        return dummy.next