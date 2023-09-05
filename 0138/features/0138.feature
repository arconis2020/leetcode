Feature: Return a deep copy of the original linked list with random pointers.

  Scenario: 1
     Given A linked list of "[[7,null],[13,0],[11,4],[10,2],[1,0]]"
      Then The result will be "[[7,null],[13,0],[11,4],[10,2],[1,0]]"

  Scenario: 2
     Given A linked list of "[[1,1],[2,1]]"
      Then The result will be "[[1,1],[2,1]]"

  Scenario: 3
     Given A linked list of "[[3,null],[3,0],[3,null]]"
      Then The result will be "[[3,null],[3,0],[3,null]]"
