from behave import *
from linked_list_cycle import Solution, ListNode
import json


@given('A linked list of "{head}" and a tail position of {pos:d}')
def step_impl(context, head, pos):
    context.sol = Solution()
    nodes = [ListNode(n) for n in json.loads(head)]
    for n in range(len(nodes) - 1):
        nodes[n].next = nodes[n + 1]
    nodes[-1].next = nodes[pos] if pos != -1 else None
    context.result = context.sol.hasCycle(nodes[0])
    print(context.result)

@then('The result will be {r}')
def step_impl(context, r):
    assert str(context.result) == r
