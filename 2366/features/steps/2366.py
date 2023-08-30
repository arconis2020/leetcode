from behave import *
from minimum_replacements import Solution
import json


@given('A nums array of "{nums}"')
def step_impl(context, nums):
    nums = json.loads(nums)
    context.sol = Solution()
    context.result = context.sol.minimumReplacement(nums)
    print(context.result)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
