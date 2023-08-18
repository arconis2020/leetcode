Feature: Return the distance to the nearest 0 for each cell.

  Scenario: 1
     Given A matrix of "[[0,0,0],[0,1,0],[0,0,0]]"
      Then The result will be "[[0,0,0],[0,1,0],[0,0,0]]"

  Scenario: 2
     Given A matrix of "[[0,0,0],[0,1,0],[1,1,1]]"
      Then The result will be "[[0,0,0],[0,1,0],[1,2,1]]"

  Scenario: 3
     Given A matrix of "[[1,1,1],[1,0,1],[1,1,1]]"
      Then The result will be "[[2,1,2],[1,0,1],[2,1,2]]"

  Scenario: 4
     Given A matrix of "[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]"
      Then The result will be "[[19,19,19],[18,18,18],[17,17,17],[16,16,16],[15,15,15],[14,14,14],[13,13,13],[12,12,12],[11,11,11],[10,10,10],[9,9,9],[8,8,8],[7,7,7],[6,6,6],[5,5,5],[4,4,4],[3,3,3],[2,2,2],[1,1,1],[0,0,0]]"
