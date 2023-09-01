from behave import *
from count_bits import Solution
import json


@given('An integer {n:d}')
def step_impl(context, n):
    context.sol = Solution()
    context.result = context.sol.countBits(n)
    print(context.result)

@then('The result will be "{r}"')
def step_impl(context, r):
    assert context.result == json.loads(r)
