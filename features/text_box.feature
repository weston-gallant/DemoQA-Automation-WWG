@regression
Feature: DemoQA Text Box coverage

  Scenario: User can submit text box form with valid data
    Given I am on the text box page
    When I fill in the text box with default user data
    And I submit the text box form
    Then I see the text box output matching the input

  Scenario Outline: User submits text box form with different valid data
    Given I am on the text box page
    When I fill the text box form for "<user_key>" from text box data
    And I submit the text box form
    Then I see the text box output matching the input

    Examples:
      | user_key   |
      | student_1  |
      | student_2  |
