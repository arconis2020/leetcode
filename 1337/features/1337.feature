Feature: Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

  Scenario: 1
     Given An input matrix of "[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]" and a k value of 3
      Then The result will be "[2,0,3]"

  Scenario: 2
     Given An input matrix of "[[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]" and a k value of 2
      Then The result will be "[0,2]"
