Feature: Reverse the LL from point left to point right and return the LL.

  Scenario: 1
     Given A linked list of "[1,2,3,4,5]" and a left of 2 and a right of 4
      Then The result will be "[1,4,3,2,5]"

  Scenario: 2
     Given A linked list of "[5]" and a left of 1 and a right of 1
      Then The result will be "[5]"

  Scenario: 3
     Given A linked list of "[1,2,3,4]" and a left of 1 and a right of 4
      Then The result will be "[4,3,2,1]"

  Scenario: 4
     Given A linked list of "[1,2,3,4]" and a left of 1 and a right of 3
      Then The result will be "[3,2,1,4]"

  Scenario: 5
     Given A linked list of "[1,2,3,4]" and a left of 2 and a right of 4
      Then The result will be "[1,4,3,2]"
