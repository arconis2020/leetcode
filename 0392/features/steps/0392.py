from behave import *
from is_subsequence import Solution


@given('A string s "{s}" and a string t "{t}"')
def step_impl(context, s, t):
    if s == "EMPTY":
        s = ""
    if t == "EMPTY":
        t = ""
    context.sol = Solution()
    context.result = context.sol.isSubsequence(s, t)
    print(context.result)


@then('The result will be "{r}"')
def step_impl(context, r):
    assert str(context.result) == r
