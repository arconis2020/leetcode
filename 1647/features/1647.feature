Feature: Return the minimum number of deletions to make a string "good"

  Scenario: 1
     Given A string of "aab"
      Then The result will be 0

  Scenario: 2
     Given A string of "aaabbbcc"
      Then The result will be 2

  Scenario: 3
     Given A string of "ceabaacb"
      Then The result will be 2

  Scenario: 4
     Given A string of "bbcebab"
      Then The result will be 2
