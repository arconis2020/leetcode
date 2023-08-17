from behave import *
from combos import Solution
import json


@given('A k value of "{k:d}" and an n value of "{n:d}"')
def step_impl(context, k, n):
    context.sol = Solution()
    context.result = context.sol.combine(n, k)
    print(context.result)

@then('The result will be "{result}"')
def step_impl(context, result):
    result = json.loads(result)
    assert context.result == result
