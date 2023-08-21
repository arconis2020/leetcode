Feature: Check if a string can be constructed by repeated substrings.

  Scenario: 1
     Given A string of "abab"
      Then The result will be True

  Scenario: 2
     Given A string of "aba"
      Then The result will be False

  Scenario: 3
     Given A string of "abcabcabcabc"
      Then The result will be True

  Scenario: 4
     Given A string of "a"
      Then The result will be False

  Scenario: 5
     Given A string of "ababab"
      Then The result will be True

  Scenario: 6
     Given A string of "abaababaab"
      Then The result will be True
