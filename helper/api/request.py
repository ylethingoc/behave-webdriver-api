from helper.api import APIBase


class SpotifyAPI(APIBase):

    def __init__(self):
        url = 'https://api.spotify.com/v1'
        super(SpotifyAPI, self).__init__(url)

    def get_album_info(self, id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
                             "BQDmbAzzOU2F-RYuYa62wuwP6BXA_NjjptPwm0tKJ50C8EbT1YdABFcl7OdT6rGccuYv1AdKvkapRakzfHCBaR44oi"
                             "SodcVZS4AUNMnYyLxmnWk2TGFc7-QB5Neb1AW4GXSYYClWrHBDutD2tYNwzy-p7WfR6fAlUpM"
        }

        url = 'albums/{}'.format(id)
        return self.get(url, headers=headers)

    def post(self, url, body):
        return self.post('warranty', body=body)

    def put(self, url, body):
        return self.put('warranty', body=body)
