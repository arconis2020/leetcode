from behave import *
from palindrome_number import Solution


@given('A number of {x:d}')
def step_impl(context, x):
    context.sol = Solution()
    context.result = context.sol.isPalindrome(x)
    print(context.result)

@then('The result will be {result}')
def step_impl(context, result):
    assert str(context.result) == result
