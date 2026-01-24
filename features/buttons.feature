@regression
Feature: DemoQA Buttons coverage
  Scenario: User can click all button types
    Given I am on the buttons page
    When I click the double click button
    And I right click the right click button  
    And I click the dynamic click button
    Then I see all button messages
