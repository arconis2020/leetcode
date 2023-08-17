Feature: Find all possible permutations of an array

  Scenario: 1
     Given A number list of "[1,2,3]"
      Then The result will be "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"

  Scenario: 2
     Given A number list of "[0,1]"
      Then The result will be "[[0,1],[1,0]]"

  Scenario: 3
     Given A number list of "[1]"
      Then The result will be "[[1]]"
