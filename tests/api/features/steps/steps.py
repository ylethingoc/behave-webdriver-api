import logging
from behave import *

from helper.api.request import SpotifyAPI

rq = SpotifyAPI()
logging.basicConfig(level=logging.INFO)


@given("We have an album_id {album_id}")
def step_impl(context, album_id):
    context.album_id = album_id
    logging.info(context.album_id)


@when("We send the request to Spotify")
def step_impl(context):
    context.response = rq.get_album_info(context.album_id)
    logging.debug(context.response.json())


@step("We verify the response status is {status_code}")
def step_impl(context, status_code):
    assert int(
        status_code) == context.response.status_code, 'Wrong status code! Detected "{}" while expected "{}"'.format(
        context.response.status_code, status_code)


@step("We get all information about this album")
def step_impl(context):
    context.artist = context.response.json()['artists'][0]['name']
    context.name = context.response.json()['name']


@step("We verify that {key} is {value}")
def step_impl(context, key, value):
    if key == 'artist':
        assert value == context.artist, 'Incorrect information! {} != {}'.format(value, context.artist)
    elif key == 'album_name':
        assert value == context.name, 'Incorrect information! {} != {}'.format(value, context.name)
