Feature: Spotify

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
