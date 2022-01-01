Feature: Spotify

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
    And We store this token into token.cfg file


  Scenario Outline: Verify some information of an album
    Given We have an album_id <album_id>
    When We send the request to Spotify
    Then We verify the response status is 200
    And We get all information about this album
    And We verify that artist is <artist>
    And We verify that album_name is <album_name>

    Examples:
      | album_id               | artist                 | album_name            |
      | 56TXgyJ5vD2F3v2pOhWFDk | Matthew Perryman Jones | Living in the Shadows |
      | 4Yf5LJfqpjgl1a4TBiCi07 | Michael Bublé          | To Be Loved           |
      | 2dzxJbiJKhQo2aqUrtjZP0 | Years & Years          | Take Shelter          |
