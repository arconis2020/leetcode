Feature: Convert a string into a 32-bit signed int.

  Scenario: 1
     Given A string of "42"
      Then The result will be 42

  Scenario: 2
     Given A string of "   -42"
      Then The result will be -42

  Scenario: 3
     Given A string of "4193 with words"
      Then The result will be 4193

  Scenario: 4
     Given A string of "+"
      Then The result will be 0

  Scenario: 5
     Given A string of "4294967296"
      Then The result will be 2147483647
