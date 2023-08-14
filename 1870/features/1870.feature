Feature: Find minimum speed on time.

  Scenario: 1
     Given A train set of "[1,3,2]" and an hour of 6
      Then The result will be 1

  Scenario: 2
     Given A train set of "[1,3,2]" and an hour of 2.7
      Then The result will be 3

  Scenario: 3
     Given A train set of "[1,3,2]" and an hour of 1.9
      Then The result will be -1

  Scenario: 3
     Given A train set of "[5,3,4,6,2,2,7]" and an hour of 10.92
      Then The result will be 4
