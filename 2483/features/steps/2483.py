from behave import *
from best_closing_time import Solution


@given('A string of "{s}"')
def step_impl(context, s):
    context.sol = Solution()
    context.result = context.sol.bestClosingTime(s)
    print(context.result)

@then('The result will be {result:d}')
def step_impl(context, result):
    assert context.result == result
