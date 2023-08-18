from behave import *
from maximal_network_rank import Solution
import json


@given('A city count of {n:d} and road list of "{roads}"')
def step_impl(context, n, roads):
    roads = json.loads(roads)
    context.sol = Solution()
    context.result = context.sol.maximalNetworkRank(n, roads)
    print(context.result)

@then('The result will be {result:d}')
def step_impl(context, result):
    assert context.result == result
