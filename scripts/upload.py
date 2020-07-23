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
        self.token = "Bearer {}".format(self.key)

    def upload(self):
        # to make request for upload form 
        path = "import/upload/"
        request_uri = "/".join([self.root,path])

        headers = {'Authorization': self.token, 'application' : 'WhiteFlip', 
                    "Content-type": "application/json",
                    'User-Agent':'https://github.com/BlankGodd/whiteflip'}
        
        response = requests.post(request_uri, headers=headers)
        if response.status_code not in range(200,300):
            return None
        return response.text

    def form(self, file_path):
        # Fill online form
        response = self.upload()
        # response.status_code = 201
        if not response:
            raise RequestError("Could not make request. Check connection")
        text = json.loads(response)
        params = text['data']['result']['form']['parameters']
        url = text['data']['result']['form']['url']
        upload_id = text['data']['id']
        file_path = "@"+file_path
        params['file'] = file_path
        redirect = params['redirect']

        headers = {'Authorization': self.token, 'application' : 'WhiteFlip', 
                    "Content-type": "application/json",
                    'User-Agent':'https://github.com/BlankGodd/whiteflip',
                    "Location": "redirect"}

        response = requests.post(url, headers=headers, data=params)
        """if response.status_code not in range(200,300):
            return None"""
        return response.status_code


