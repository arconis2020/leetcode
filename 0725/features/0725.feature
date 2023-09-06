Feature: Split the linked list into k consecutive linked lists following size rules.

  Scenario: 1
     Given A linked list of "[1,2,3]" and a k value of 5
      Then The result will be "[[1],[2],[3],[],[]]"

  Scenario: 2
     Given A linked list of "[1,2,3,4,5,6,7,8,9,10]" and a k value of 3
      Then The result will be "[[1,2,3,4],[5,6,7],[8,9,10]]"

  Scenario: 3
     Given A linked list of "[]" and a k value of 50
      Then The result will be "[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]"
