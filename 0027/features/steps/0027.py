from behave import *
from remove_element import Solution
import json


@given('A number list of "{nums}" and a value of {val:d}')
def step_impl(context, nums, val):
    nums = json.loads(nums)
    context.sol = Solution()
    context.result = context.sol.removeElement(nums, val)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
