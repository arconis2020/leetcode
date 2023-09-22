Feature: Return True if s is a subsequence of t

  Scenario: 1
     Given A string s "abc" and a string t "ahbgdc"
      Then The result will be "True"

  Scenario: 2
     Given A string s "axc" and a string t "ahbgdc"
      Then The result will be "False"

  Scenario: 3
     Given A string s "EMPTY" and a string t "EMPTY"
      Then The result will be "True"
