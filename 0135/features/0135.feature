Feature: Return the minimum candies you need to distribute candy based on the rules.

  Scenario: 1
     Given A ratings list of "[1,0,2]"
      Then The result will be 5

  Scenario: 2
     Given A ratings list of "[1,2,2]"
      Then The result will be 4

  Scenario: 3
     Given A ratings list of "[1,2,87,87,87,2,1]"
      Then The result will be 13

  Scenario: 4
     Given A ratings list of "[1,2,87,4,3,2,1]"
      Then The result will be 18

  Scenario: 5
     Given A ratings list of "[0]"
      Then The result will be 1

  Scenario: 6
     Given A ratings list of "[]"
      Then The result will be 0
