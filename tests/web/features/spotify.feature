Feature: Spotify

  Scenario: Visit Spotify develop website then get the OAuth Token
    Given We have a Spotify's user and password
    When We visit https://developer.spotify.com/console/get-artist/
    And We hit on GET_TOKEN button
    And We hit on REQUEST_TOKEN button
    Then We navigate to LOGIN page
    When We input user and password to login
    And We hit on LOGIN button
    Then We navigate to ACCEPT page
    When We hit on ACCEPT button
    Then We get the OAuth Token
    And We store this Token into setup.cfg file