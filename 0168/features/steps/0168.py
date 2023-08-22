from behave import *
from excel_column_title import Solution


@given('A column number of {columnNumber:d}')
def step_impl(context, columnNumber):
    context.sol = Solution()
    context.result = context.sol.convertToTitle(columnNumber)
    print(context.result)

@then('The result will be "{result}"')
def step_impl(context, result):
    assert context.result == result
