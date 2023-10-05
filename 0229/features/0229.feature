Feature: Find all elements that appear more than n/3 times.

  Scenario: 1
     Given A nums list of "[3,2,3]"
      Then The result will be "[3]"

  Scenario: 2
     Given A nums list of "[1]"
      Then The result will be "[1]"

  Scenario: 3
     Given A nums list of "[1,2]"
      Then The result will be "[1,2]"

  Scenario: 4
     Given A nums list of "[2,2]"
      Then The result will be "[2]"

  Scenario: 5
     Given A nums list of "[1,2,3]"
      Then The result will be "[]"

  Scenario: 6
     Given A nums list of "[2,2,1,3]"
      Then The result will be "[2]"

  Scenario: 7
     Given A nums list of "[1,1,2]"
      Then The result will be "[1]"

  Scenario: 8
     Given A nums list of "[1,1,2,2]"
      Then The result will be "[1,2]"

  Scenario: 9
     Given A nums list of "[3,3,1,1,1,1,2,4,4,3,3,3,4,4]"
      Then The result will be "[3]"

  Scenario: 10
     Given A nums list of "[3,2,2,2,3]"
      Then The result will be "[2,3]"
