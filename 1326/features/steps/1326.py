from behave import *
from minimum_taps import Solution
import json


@given('A taps array of "{ranges}" and a garden length of {n:d}')
def step_impl(context, n, ranges):
    ranges = json.loads(ranges)
    context.sol = Solution()
    context.result = context.sol.minTaps(n, ranges)
    print(context.result)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
