"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        prev = dummy
        temp = head 
        maps_old = defaultdict(int)
        maps_new = defaultdict(None)

        curr = 0

        while temp:
            new_node = Node(temp.val)
            maps_old[temp] = curr
            maps_new[curr] = new_node

            prev.next = new_node
            prev = new_node
            temp = temp.next
            curr += 1

        #filling random vals:
        temp = head
        curr = 0
        while temp:
            old_random = temp.random
            new_random = None

            if old_random is not None:
                old_random_ind = maps_old[old_random]
                new_random = maps_new[old_random_ind]
                
            maps_new[curr].random = new_random
            curr += 1
            temp = temp.next

        return dummy.next

