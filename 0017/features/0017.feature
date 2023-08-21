Feature: Convert a string of numbers into its possible phone dialer letter combinations.

  Scenario: 1
     Given A string of "23"
      Then The result will be ;["ad","ae","af","bd","be","bf","cd","ce","cf"];

  Scenario: 2
     Given A string of "emptystr"
      Then The result will be ;[];

  Scenario: 3
     Given A string of "2"
      Then The result will be ;["a","b","c"];

  Scenario: 4
     Given A string of "2345"
      Then The result will be ;["adgj","adgk","adgl","adhj","adhk","adhl","adij","adik","adil","aegj","aegk","aegl","aehj","aehk","aehl","aeij","aeik","aeil","afgj","afgk","afgl","afhj","afhk","afhl","afij","afik","afil","bdgj","bdgk","bdgl","bdhj","bdhk","bdhl","bdij","bdik","bdil","begj","begk","begl","behj","behk","behl","beij","beik","beil","bfgj","bfgk","bfgl","bfhj","bfhk","bfhl","bfij","bfik","bfil","cdgj","cdgk","cdgl","cdhj","cdhk","cdhl","cdij","cdik","cdil","cegj","cegk","cegl","cehj","cehk","cehl","ceij","ceik","ceil","cfgj","cfgk","cfgl","cfhj","cfhk","cfhl","cfij","cfik","cfil"];
