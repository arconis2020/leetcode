from behave import *
from atoi import Solution


@given('A string of "{s}"')
def step_impl(context, s):
    context.sol = Solution()
    context.result = context.sol.myAtoi(s)
    print(context.result)

@then('The result will be {result:d}')
def step_impl(context, result):
    assert context.result == result
