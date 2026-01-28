@regression
Feature: DemoQA Buttons interactions

  Scenario: Double click shows correct message
    Given I am on the buttons page
    Then I do not see any button messages
    When I click the double click button
    Then I see the double click message only

  Scenario: Right click shows correct message
    Given I am on the buttons page
    Then I do not see any button messages
    When I right click the right click button
    Then I see the right click message only

  Scenario: Dynamic click shows correct message
    Given I am on the buttons page
    Then I do not see any button messages
    When I click the dynamic click button
    Then I see the dynamic click message only
