@regression
Feature: DemoQA Practice form coverage

  Scenario: User can submit a practice form with required fields
    Given I am on the practice forms page
    When I fill in the required fields
    Then I see a success message
    And I close the modal

  Scenario: User sees error when required fields are empty
    Given I am on the practice forms page
    When I submit the form without filling required fields
    Then I see validation errors for required fields

  Scenario Outline: User submits practice form with different valid data
    Given I am on the practice forms page
    When I fill the practice form for "<user_key>" from practice form data
    Then I see a success message
    And I close the modal

    Examples:
      | user_key   |
      | student_1  |
      | student_2  |
