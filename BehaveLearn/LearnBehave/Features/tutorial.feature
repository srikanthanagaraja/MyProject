Feature:Calculator

  Scenario Outline: Printing outline
	Given we have behave installed
	When we implement scenario outline
    Then <a> and <b> should be printed
  Examples:
	|a|b|
	|2|4|
	|6|8|
  
  @slow
  Scenario: Understanding of Behave
	Given we have behave installed
	When we implement a test
	Then behave will test it for us