from behave import *
from copy_list import Solution, Node
import json


def list_to_node(list_str):
    items = json.loads(list_str)
    nodes = [Node(x[0]) for x in items]
    for n in range(len(nodes) - 1):
        nodes[n].next = nodes[n + 1]
    for m in range(len(items)):
        if items[m][1] is not None:
            nodes[m].random = nodes[items[m][1]]
    return nodes[0]


@given('A linked list of "{head}"')
def step_impl(context, head):
    context.sol = Solution()
    head = list_to_node(head)
    context.result = context.sol.copyRandomList(head)
    print(context.result)

@then('The result will be "{r}"')
def step_impl(context, r):
    assert str(context.result) == str(list_to_node(r))
