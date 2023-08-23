from behave import *
from reorganize import Solution


@given('A string of "{s}"')
def step_impl(context, s):
    context.sol = Solution()
    context.result = context.sol.reorganizeString(s)
    print(context.result)

@then('The result will be "{result}"')
def step_impl(context, result):
    if result == "emptystr":
        result = ""
    assert context.result == result
