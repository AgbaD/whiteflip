#!usr/bin/python
# Author:   @BlankGodd_

import requests
import os
import json

class RequestError(Exception):
    pass

class Upload:

    def __init__(self,key):
        self.key = key
        self.root = "https://api.cloudconvert.com/v2"

    def upload(self):
        # to make request for upload form 
        path = "import/upload/"
        request_uri = "/".join([self.root,path])

        token = "Bearer {}".format(self.key)
        headers = {'Authorization': token, 
                    'application' : 'WhiteFlip', "Content-type": "application/json",
                    'User-Agent':'https://github.com/BlankGodd/whiteflip'}
        
        response = requests.post(request_uri, headers=headers)
        if response.status_code not in range(200,300):
            print(response.status_code)
            return None
        return response.text

    def form(self, file_path=None):
        response = self.upload()
        if not response:
            raise RequestError("Could not make request. Check connection")
        text = json.loads(response)
        return text

