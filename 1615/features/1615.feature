Feature: Find the maximal network rank of the entire infrastructure.

  Scenario: 1
     Given A city count of 4 and road list of "[[0,1],[0,3],[1,2],[1,3]]"
      Then The result will be 4

  Scenario: 2
     Given A city count of 5 and road list of "[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]"
      Then The result will be 5

  Scenario: 3
     Given A city count of 8 and road list of "[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]"
      Then The result will be 5

  Scenario: 4
     Given A city count of 2 and road list of "[[1,0]]"
      Then The result will be 1
