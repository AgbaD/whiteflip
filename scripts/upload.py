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

    def upload(self,file_path):
        # to make request for upload form 
        path = "jobs"
        request_uri = "/".join([self.root,path])

        headers = {'Authorization': self.token, 
                    'application' : 'WhiteFlip', 
                    "Content-type": "application/json",
                    'User-Agent':'https://github.com/BlankGodd/whiteflip'}
        
        data = {
                "tasks": {
                    "import-1": {
                        "operation": "import/upload",
                        "file": file_path
                    }
                }
            }
        
        response = requests.post(request_uri, include=data, 
                    headers=headers)
        """if response.status_code not in range(200,300):
            return None"""
        return (response.status_code, response.text)

    


