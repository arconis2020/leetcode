from behave import *
from permute import Solution
import json


@given('A number list of "{nums}"')
def step_impl(context, nums):
    nums = json.loads(nums)
    context.sol = Solution()
    context.result = context.sol.permute(nums)
    print(context.result)

@then('The result will be "{result}"')
def step_impl(context, result):
    result = json.loads(result)
    assert sorted(context.result) == sorted(result)
