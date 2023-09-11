Feature: Group the people given the group size they belong to.

  Scenario: 1
     Given A groupSizes list of "[3,3,3,3,3,1,3]"
      Then The result will be "[[5],[0,1,2],[3,4,6]]"

  Scenario: 2
     Given A groupSizes list of "[2,1,3,3,3,2]"
      Then The result will be "[[1],[0,5],[2,3,4]]"
