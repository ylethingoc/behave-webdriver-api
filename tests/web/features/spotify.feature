Feature: Spotify Web

  Scenario: Visit Spotify develop website then get the OAuth Token
    Given We have a Spotify's user and password
    When We visit Spotify Develop website
    And We hit on the GET_TOKEN button
    And We hit on the REQUEST_TOKEN button
    Then We navigate to LOGIN page
    When We input user and password to login
    And We hit on the LOGIN button
    Then We navigate to ACCEPT page
    When We hit on the ACCEPT button
    Then We get the OAuth Token
    And We store this token into setup.cfg file