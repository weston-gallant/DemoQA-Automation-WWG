@regression
Feature: DemoQA Alerts coverage

  Scenario: User can accept a simple alert
    Given I am on the alerts page
    When I trigger the simple alert
    Then I can accept the simple alert

  Scenario: User can accept a delayed alert
    Given I am on the alerts page
    When I trigger the delayed alert
    Then I can accept the delayed alert when it appears

  Scenario: User can accept a confirm alert
    Given I am on the alerts page
    When I trigger the confirm alert
    And I accept the confirm alert
    Then I see the confirm result text "You selected Ok"

  Scenario: User can dismiss a confirm alert
    Given I am on the alerts page
    When I trigger the confirm alert
    And I dismiss the confirm alert
    Then I see the confirm result text "You selected Cancel"

  Scenario Outline: User can enter text into a prompt alert
    Given I am on the alerts page
    When I trigger the prompt alert
    And I enter "<name>" into the prompt alert
    Then I see the prompt result text "You entered <name>"

    Examples:
      | name      |
      | Weston    |
      | Automation |

  Scenario: User dismisses the prompt alert and sees no result
    Given I am on the alerts page
    When I trigger the prompt alert
    And I enter "DismissMe" into the prompt alert but dismiss it
    Then I do not see any prompt result text
