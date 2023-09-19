from behave import *
from find_duplicate import Solution
import json


@given('A nums list of "{nums}"')
def step_impl(context, nums):
    context.sol = Solution()
    nums = json.loads(nums)
    context.result = context.sol.findDuplicate(nums)
    print(context.result)


@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
