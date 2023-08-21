from behave import *
from letter_combinations_of_a_phone_number import Solution
import json


@given('A string of "{s}"')
def step_impl(context, s):
    if s == "emptystr":
        s = ""
    context.sol = Solution()
    context.result = context.sol.letterCombinations(s)
    print(context.result)

@then('The result will be ;{result};')
def step_impl(context, result):
    result = json.loads(result)
    assert context.result == result
