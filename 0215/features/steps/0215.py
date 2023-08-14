from behave import *
from kth_largest_element import Solution
import json
import random


@given('A an array of "{nums}" and a k value of {k:d}')
def step_impl(context, nums, k):
    if nums == "max":
        nums = random.choices(range(-10**4, 10**4+1), k=10**5)
    else:
        nums = json.loads(nums)
    context.nums = nums
    context.k = k
    context.sol = Solution()
    context.result = context.sol.findKthLargest(nums, k)
    print(context.result)

@then('The result will be calculated.')
def step_impl(context):
    exp = sorted(context.nums)[-context.k]
    print(exp)
    assert context.result == exp
