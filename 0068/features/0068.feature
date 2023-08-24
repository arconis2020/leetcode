Feature: Justify an array of strings to maxWidth using an output list. The last line should be left-justified.

  Scenario: 1
     Given A list of words ;["This", "is", "an", "example", "of", "text", "justification."]; and a maxWidth of 16
      Then The result will be ;["This    is    an", "example  of text", "justification.  "];

  Scenario: 2
     Given A list of words ;["What","must","be","acknowledgment","shall","be"]; and a maxWidth of 16
      Then The result will be ;["What   must   be", "acknowledgment  ", "shall be        "];

  Scenario: 3
     Given A list of words ;["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]; and a maxWidth of 20
      Then The result will be ;["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "];
