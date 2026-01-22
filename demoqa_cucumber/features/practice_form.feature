Feature: Test
  Scenario: Simple test
    Given I am on the practice forms page
    When I fill in the required fields
    Then I see a success message
    Then I close the modal