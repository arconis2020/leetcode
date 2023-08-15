from behave import *
from find_smallest_missing import Solution
import json


@given('An integer array of "{nums}" and a value of {value:d}')
def step_impl(context, nums, value):
    nums = json.loads(nums)
    context.sol = Solution()
    context.result = context.sol.findSmallestInteger(nums, value)
    print(context.result)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
