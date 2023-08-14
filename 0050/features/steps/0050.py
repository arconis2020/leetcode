from behave import *
from power import Solution


@given('A base of {x:f} and an exponent of {n:d}')
def step_impl(context, x, n):
    context.sol = Solution()
    context.result = context.sol.myPow(x, n)

@then('The result will be {r}')
def step_impl(context, r):
    assert f"{context.result:.5f}" == r
