from typing import Optional
import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


class Solution:
    def unwind(self, n: Optional[ListNode]) -> list[int]:
        if not n:
            return []
        retlist = [n.val]
        while n.next is not None:
            retlist.append(n.next.val)
            n = n.next
        return retlist

    def wind(self, n: list[int]) -> Optional[ListNode]:
        if not n:
            return None
        nodes = [ListNode(x) for x in n]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        retlist = [None] * k
        proto_list = self.unwind(head)
        new_len, rem = divmod(len(proto_list), k)
        for n in range(rem):
            retlist[n], proto_list = self.wind(proto_list[:new_len + 1]), proto_list[new_len + 1:]
        for n in range(rem, len(retlist)):
            retlist[n], proto_list = self.wind(proto_list[:new_len]), proto_list[new_len:]
        return retlist
