from behave import *
from split import Solution, ListNode
import json


@given('A linked list of "{head}" and a k value of {k:d}')
def step_impl(context, head, k):
    context.sol = Solution()
    head = context.sol.wind(json.loads(head))
    context.result = context.sol.splitListToParts(head, k)

@then('The result will be "{r}"')
def step_impl(context, r):
    r = [context.sol.wind(x) for x in json.loads(r)]
    assert context.result == r
