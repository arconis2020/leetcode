from behave import *
from trains import Solution
import json


@given('A train set of "{dist}" and an hour of {hour:g}')
def step_impl(context, dist, hour):
    dist = json.loads(dist)
    context.sol = Solution()
    context.result = context.sol.minSpeedOnTime(dist, hour)
    print(context.result)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
