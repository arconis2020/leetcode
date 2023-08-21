from behave import *
from substring import Solution


@given('A string of "{s}"')
def step_impl(context, s):
    context.sol = Solution()
    context.result = context.sol.repeatedSubstringPattern(s)
    print(context.result)

@then('The result will be {result}')
def step_impl(context, result):
    assert str(context.result) == result
