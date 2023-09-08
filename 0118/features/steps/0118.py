from behave import *
from pascal import Solution
import json


@given('A numRows value of {numRows:d}')
def step_impl(context, numRows):
    context.sol = Solution()
    context.result = context.sol.generate(numRows)

@then('The result will be "{r}"')
def step_impl(context, r):
    assert context.result == json.loads(r)
