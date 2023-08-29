Feature: Find the best hour in which to close the shop.

  Scenario: 1
     Given A string of "YYNY"
      Then The result will be 2

  Scenario: 2
     Given A string of "NNNNN"
      Then The result will be 0

  Scenario: 3
     Given A string of "YYYY"
      Then The result will be 4

  Scenario: 4
     Given A string of "YN"
      Then The result will be 1
