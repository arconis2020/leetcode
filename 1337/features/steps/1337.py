from behave import *
from k_weakest_rows import Solution
import json


@given('An input matrix of "{mat}" and a k value of {k:d}')
def step_impl(context, mat, k):
    context.sol = Solution()
    mat = json.loads(mat)
    context.result = context.sol.kWeakestRows(mat, k)
    print(context.result)


@then('The result will be "{r}"')
def step_impl(context, r):
    assert context.result == json.loads(r)
