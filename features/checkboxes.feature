@regression
Feature: DemoQA Check Box coverage

  Scenario: User can expand all and select Home
    Given I am on the check box page
    When I expand all check boxes
    And I select the "Home" checkbox
    Then I see "home" in the selected results

  Scenario: User can select multiple leaf check boxes
    Given I am on the check box page
    When I expand all check boxes
    And I select the following check boxes
      | label      |
      | Desktop    |
      | Documents  |
      | Downloads  |
    Then I see all of these in the selected results
      | result_key |
      | desktop    |
      | documents  |
      | downloads  |

  Scenario Outline: User selects a single check box from data
    Given I am on the check box page
    When I expand all check boxes
    And I select the "<label>" checkbox from check box data
    Then I see "<result_key>" in the selected results

    Examples:
      | label     | result_key |
      | Desktop   | desktop    |
      | Documents | documents  |
      | Downloads | downloads  |
