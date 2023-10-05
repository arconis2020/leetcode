from behave import *
from majority_element import Solution
import json


@given('A nums list of "{nums}"')
def step_impl(context, nums):
    context.sol = Solution()
    nums = json.loads(nums)
    context.result = context.sol.majorityElement(nums)
    print(context.result)


@then('The result will be "{r}"')
def step_impl(context, r):
    assert context.result == json.loads(r)
