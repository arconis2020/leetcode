from behave import *
from computers import Solution
import json


@given('A battery array of "{batteries}" and a computer count of {n:d}')
def step_impl(context, batteries, n):
    batteries = json.loads(batteries)
    context.sol = Solution()
    context.result = context.sol.maxRunTime(n, batteries)
    print(context.result)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
