Feature: Spotify API

  Scenario: Verify some information of an album
    Given We have an album_id
    When We send the request to Spotify
    Then We verify the response status is 200
    And We get all information about this album
    And We verify that artist is Matthew Perryman Jones
    And We verify that album_name is Living in the Shadows
