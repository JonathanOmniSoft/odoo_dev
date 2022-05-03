# -*- coding: utf-8 -*-
import os
import json
import lazop

# Param
url = "https://api.lazada.sg/rest"
appkey = "108986"
appSecret = "GbDUTQw7T2qzRG0hmfsvthSQO213QaM0"
access_token = "50000200309bbhqacuxDw125aa93dlknuvmwCB3oYGjQCRSh8cdvhrwTcI8brSJu"


class product():
    def __init__(self):
        self.client = lazop.LazopClient(url, appkey ,appSecret)

    def Create(self):
        self.request = lazop.LazopRequest('/product/create')
        self.add_param('ADD', 'create_product.xml')

    def AdjustSellableQuantity(self):
        self.request = lazop.LazopRequest('/product/stock/sellable/adjust')
        self.add_param('UPDATE', 'quantity.xml')  
    
    def Remove(self, product_list):
        self.request = lazop.LazopRequest('/product/remove')
        sku_list = []
        for sku in product_list:
            skuid = "SkuId_" + sku["itemid"] + "_" + sku["skuid"]
            sku_list.append(skuid)
        json_string = json.dumps(sku_list)
            
        self.add_param('REMOVE', json_string)

    def GetAll(self):
        self.request = lazop.LazopRequest('/products/get','GET')
        self.request.add_api_param('filter', 'live')
        self.request.add_api_param('create_before', '2018-01-01T00:00:00+0800')
        self.request.add_api_param('update_before', '2018-01-01T00:00:00+0800')
        self.request.add_api_param('offset', '0')
        self.request.add_api_param('create_after', '2010-01-01T00:00:00+0800')
        self.request.add_api_param('update_after', '2010-01-01T00:00:00+0800')
        self.request.add_api_param('limit', '10')
        self.request.add_api_param('options', '1')
        self.request.add_api_param('sku_seller_list', ' [\"39817:01:01\", \"Apple 6S Black\"]')
        response = self.client.execute(request, access_token)
        print(response.type)
        print(response.body)


    # Helper function
    def add_param(self, action, xml):
        if action.upper() == 'REMOVE':
            self.request.add_api_param('seller_sku_list', xml)
        else:
            dir_path = '/Users/xt/Documents/work/tasp/tasp/'
            self.request.add_file_param('file_bytes',open(os.path.join(dir_path, xml).read()))
            self.request.add_api_param('payload', xml)
        self.submit_request()

    def submit_request(self):
        # Get Access Token
        self.response = self.client.execute(self.request, access_token)
        print(self.response.type)
        print(self.response.body)
        return 'Successful'

