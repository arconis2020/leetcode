from behave import *
from matrix import Solution
import json


@given('A matrix of "{matrix}"')
def step_impl(context, matrix):
    matrix = json.loads(matrix)
    context.sol = Solution()
    context.result = context.sol.updateMatrix(matrix)
    print(context.result)

@then('The result will be "{result}"')
def step_impl(context, result):
    result = json.loads(result)
    assert context.result == result
