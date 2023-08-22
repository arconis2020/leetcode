Feature: Convert a column number to an excel column header name

  Scenario: 1
     Given A column number of 1
      Then The result will be "A"

  Scenario: 2
     Given A column number of 28
      Then The result will be "AB"

  Scenario: 3
     Given A column number of 26
      Then The result will be "Z"

  Scenario: 4
     Given A column number of 130
      Then The result will be "DZ"

  Scenario: 5
     Given A column number of 701
      Then The result will be "ZY"

  Scenario: 6
     Given A column number of 702
      Then The result will be "ZZ"

  Scenario: 7
     Given A column number of 1024
      Then The result will be "AMJ"

  Scenario: 8
     Given A column number of 2147483647
      Then The result will be "FXSHRXW"

  Scenario: 9
     Given A column number of 27
      Then The result will be "AA"

  Scenario: 10
     Given A column number of 703
      Then The result will be "AAA"

  Scenario: 11
     Given A column number of 53
      Then The result will be "BA"
