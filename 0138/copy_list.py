from typing import Optional
import json


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        retlist = []
        nodelist = []
        this_node = self
        while this_node is not None:
            retlist.append([this_node.val, this_node.random])
            nodelist.append(this_node)
            this_node = this_node.next
        for node in retlist:
            if node[1] is not None:
                node[1] = nodelist.index(node[1])
        return json.dumps(retlist)


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        this_node = head
        # Interleave the new nodes
        while this_node is not None:
            this_node.next = Node(this_node.val, this_node.next)
            this_node = this_node.next.next
        # Iterate through and update pointers
        if head.random is not None:
            head.next.random = head.random.next
        this_node = head.next # Start at A'
        while this_node.next is not None:
            # If B has a random
            if this_node.next.random is not None:
                # Set B' to that random
                this_node.next.next.random = this_node.next.random.next
            # Remove B and keep B' as next
            this_node.next = this_node.next.next
            this_node = this_node.next
        return head.next
