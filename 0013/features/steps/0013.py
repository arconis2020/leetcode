from behave import *
from romans import Solution


@given('An input of "{s}"')
def step_impl(context, s):
    context.sol = Solution()
    context.result = context.sol.romanToInt(s)

@then('The result will be {r:d}')
def step_impl(context, r):
    print(type(context.result), type(r))
    assert context.result == r
