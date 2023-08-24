from behave import *
from justify import Solution
import json


@given('A list of words ;{words}; and a maxWidth of {maxWidth:d}')
def step_impl(context, words, maxWidth):
    words = json.loads(words)
    context.sol = Solution()
    context.result = context.sol.fullJustify(words, maxWidth)
    print(context.result)

@then('The result will be ;{result};')
def step_impl(context, result):
    result = json.loads(result)
    assert context.result == result
