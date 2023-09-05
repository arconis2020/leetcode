Feature: Return True of the list cycles, False if not.

  Scenario: 1
     Given A linked list of "[3,2,0,-4]" and a tail position of 1
      Then The result will be True

  Scenario: 2
     Given A linked list of "[1,2]" and a tail position of 0
      Then The result will be True

  Scenario: 3
     Given A linked list of "[1]" and a tail position of -1
      Then The result will be False
