from behave import *
from median import Solution
import json


@given('nums1 is "{nums1}" and nums2 is "{nums2}"')
def step_impl(context, nums1, nums2):
    context.sol = Solution()
    nums1 = json.loads(nums1)
    nums2 = json.loads(nums2)
    context.result = context.sol.findMedianSortedArrays(nums1, nums2)
    print(context.result)


@then('The result will be {r:g}')
def step_impl(context, r):
    assert context.result == r
