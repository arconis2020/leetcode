from behave import *
from min_ops import Solution
import json


@given('A nums list of "{nums}" and an X value of {x:d}')
def step_impl(context, nums, x):
    context.sol = Solution()
    nums = json.loads(nums)
    context.result = context.sol.minOperations(nums, x)
    print(context.result)


@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
