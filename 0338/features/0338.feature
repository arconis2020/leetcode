Feature: Return an array of n+1 where each index is the number of 1's in the binary representation of the index.

  Scenario: 1
     Given An integer 2
      Then The result will be "[0,1,1]"

  Scenario: 2
     Given An integer 5
      Then The result will be "[0,1,1,2,1,2]"
