
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # First pass: create copies of all nodes
        temp = head

        while temp:
            old_to_new[temp] = Node(temp.val)
            temp = temp.next

        # Second pass: connect next and random pointers
        temp = head

        while temp:
            new_node = old_to_new[temp]

            new_node.next = old_to_new.get(temp.next)
            new_node.random = old_to_new.get(temp.random)

            temp = temp.next

        return old_to_new[head]
