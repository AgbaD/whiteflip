#!usr/bin/python
# Author:   @BlankGodd_

import requests
import os
import json

class RequestError(Exception):
    pass

class KeyError(Exception):
    pass

class Upload:

    def __init__(self,key):
        if not key:
            raise KeyError("Key not found!")    
        self.key = key
        self.root = "https://api.cloudconvert.com/v2"
        self.token = "Bearer {}".format(self.key)

    def upload(self,file_path):
        # to make request for upload form 
        session = requests.session()
        path = "import/url"
        request_uri = "/".join([self.root,path])

        headers = {'Authorization': self.token, 
                    'application' : 'WhiteFlip', 
                    "Content-type": "application/json",
                    'User-Agent':'https://github.com/BlankGodd/whiteflip'}
        
        data = {
            "url": "https://github.com/BlankGodd/whiteflip/blob/master/try.txt",
            "filename": "try.txt"
        }
        
        response = session.post(request_uri, data=data, 
                    headers=headers)
        """if response.status_code not in range(200,300):
            return None"""
        return (response.status_code, response.text)

    


