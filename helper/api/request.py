import os
from configparser import ConfigParser

from helper.api import APIBase
from helper import constants


class SpotifyAPI(APIBase):

    def __init__(self):
        super(SpotifyAPI, self).__init__(constants.SPOTIFY_API)

    def get_album_info(self, id):
        config = ConfigParser()
        my_file = os.path.join(os.getcwd(), 'token.cfg')
        config.read(my_file)
        token = config.get('spotify', 'token')

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(token)
        }

        url = 'albums/{}'.format(id)
        return self.get(url, headers=headers)

    def post(self, url, body):
        return self.post('warranty', body=body)

    def put(self, url, body):
        return self.put('warranty', body=body)
