from behave import *
from candy import Solution
import json


@given('A ratings list of "{ratings}"')
def step_impl(context, ratings):
    context.sol = Solution()
    ratings = json.loads(ratings)
    context.result = context.sol.candy(ratings)
    print(context.result)


@then("The result will be {r:d}")
def step_impl(context, r):
    assert context.result == r
