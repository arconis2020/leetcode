Feature: Return the first numRows of Pascal's triangle

  Scenario: 1
     Given A numRows value of 1
      Then The result will be "[[1]]"

  Scenario: 2
     Given A numRows value of 2
      Then The result will be "[[1],[1,1]]"

  Scenario: 3
     Given A numRows value of 3
      Then The result will be "[[1],[1,1],[1,2,1]]"

  Scenario: 4
     Given A numRows value of 4
      Then The result will be "[[1],[1,1],[1,2,1],[1,3,3,1]]"

  Scenario: 5
     Given A numRows value of 5
      Then The result will be "[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"
