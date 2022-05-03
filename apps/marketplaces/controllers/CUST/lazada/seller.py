# -*- coding: utf-8 -*-
from os import access
import lazop

# Get Param from database
url = "https://api.lazada.sg/rest"
appkey = "108986"
appSecret = "GbDUTQw7T2qzRG0hmfsvthSQO213QaM0"
access_token = "50000200309bbhqacuxDw125aa93dlknuvmwCB3oYGjQCRSh8cdvhrwTcI8brSJu"


class seller():
    def __init__(self):
        self.client = lazop.LazopClient(url, appkey ,appSecret)
        
    def get_seller(self):
        self.request = lazop.LazopRequest('/seller/get', 'GET') # GET Method

    def submit_request(self):
        # Get Access Token
        self.response = self.client.execute(self.request, access_token)
        print(self.response.type)
        print(self.response.body)
