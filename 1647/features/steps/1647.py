from behave import *
from minimum_deletions import Solution


@given('A string of "{s}"')
def step_impl(context, s):
    context.sol = Solution()
    context.result = context.sol.minDeletions(s)
    print(context.result)

@then('The result will be {r:d}')
def step_impl(context, r):
    assert context.result == r
