@regression
Feature: DemoQA Practice form coverage
  Scenario: User can submit a practice form with required fields
    Given I am on the practice forms page
    When I fill in the required fields
    Then I see a success message
    And I close the modal