Feature: SELENIUM

  Scenario: Visit any website then verify title
    When We visit dev.to
    Then It should have a title "DEV Community"