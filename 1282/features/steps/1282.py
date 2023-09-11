from behave import *
from group_people import Solution
import json


@given('A groupSizes list of "{groupSizes}"')
def step_impl(context, groupSizes):
    context.sol = Solution()
    groupSizes = json.loads(groupSizes)
    context.result = context.sol.groupThePeople(groupSizes)
    print(context.result)

@then('The result will be "{r}"')
def step_impl(context, r):
    assert sorted(context.result) == sorted(json.loads(r))
