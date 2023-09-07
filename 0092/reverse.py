import cProfile
import random
from typing import Optional
import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

    def __eq__(self, other):
        if self.val != other.val:
            return False
        if self.next is None and other.next is not None:
            return False
        if self.next is not None and other.next is None:
            return False
        if self.next is None and other.next is None:
            return True
        return self.next.__eq__(other.next)

    def __str__(self):
        if self.val is None:
            return '[]'
        retlist = []
        this_node = self
        while this_node is not None:
            retlist.append(this_node.val)
            this_node = this_node.next
        return json.dumps(retlist)


class Solution:
    def wind(self, n: list[int]) -> Optional[ListNode]:
        if not n:
            return None
        nodes = [ListNode(x) for x in n]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummies = [ListNode(None) for _ in range(left, right + 1)]
        dummies.insert(0, None)  # Deal with 1-index
        idx = 1
        this_node = head
        while this_node is not None and idx <= right:
            real_next = this_node.next
            if idx < left:
                dummies.insert(0, None)
            if left <= idx < right:
                new_idx = right - (idx - left)
                dummies[new_idx].val = this_node.val
                dummies[idx].next = dummies[idx + 1]
            if idx == right:
                dummies[left].val = this_node.val
                dummies[right].next = this_node.next
            if idx == left - 1:
                this_node.next = dummies[left]
            idx += 1
            this_node = real_next
        return dummies[1] if left == 1 else head


if __name__ == "__main__":
    head = random.choices(range(-500, 501), k=500)
    s = Solution()
    head = s.wind(head)
    left = 1
    right = 500
    pr = cProfile.Profile()
    pr.enable()
    for _ in range(1000):
        s.reverseBetween(head, left, right)
    pr.disable()
    pr.dump_stats("./stats")
