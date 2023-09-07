from behave import *
from reverse import Solution, ListNode
import json


@given('A linked list of "{head}" and a left of {left:d} and a right of {right:d}')
def step_impl(context, head, left, right):
    context.sol = Solution()
    head = context.sol.wind(json.loads(head))
    context.result = context.sol.reverseBetween(head, left, right)

@then('The result will be "{r}"')
def step_impl(context, r):
    r = context.sol.wind(json.loads(r))
    assert context.result == r
