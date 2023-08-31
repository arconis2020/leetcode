Feature: Find the minimum number of operations to make an array that is sorted in non-decreasing order.

  Scenario: 1
     Given A taps array of "[3,4,1,1,0,0]" and a garden length of 5
      Then The result will be 1

  Scenario: 2
     Given A taps array of "[0,0,0,0]" and a garden length of 3
      Then The result will be -1

  Scenario: 3
     Given A taps array of "[1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]" and a garden length of 35
      Then The result will be 6

  Scenario: 4
     Given A taps array of "[2,1,2,1,2,4,3,0,1,0,5,2]" and a garden length of 11
      Then The result will be 3
