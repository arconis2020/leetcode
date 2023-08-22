from behave import *
from word_break import Solution
import json


@given('A string of "{s}" and a wordDict of ;{wordDict};')
def step_impl(context, s, wordDict):
    wordDict = json.loads(wordDict)
    context.sol = Solution()
    context.result = context.sol.wordBreak(s, wordDict)
    print(context.result)

@then('The result will be {result}')
def step_impl(context, result):
    assert str(context.result) == result
