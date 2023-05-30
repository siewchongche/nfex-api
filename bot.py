# requirement:
# Could you help build another simple bot on top of this where it scans the mid and posts offer at +2%
# and it refreshes every x seconds and posts another offer at +2% of the new mid
# we want to be able to run this function using the API for our NFT perps trading basically
# default to open short, cross margin, lever 5x

import requests
import time
from dotenv import load_dotenv
load_dotenv()
import os
import hmac
import hashlib
from ed25519 import SigningKey
import json
from rich import print_json


## ================================================== user interact section ==================================================

trade_pair_id = 1002
size = '0.005' # minimum size for open short is 0.005 eth
refresh_seconds = 5 # 5 seconds
api_key = 'd202565e3bd8c4d4b6bdd21c4e1133ef3f6ab7c6fc6b638cbe2d4d7d05460c9c'

## =============================================== end of user interact section ===============================================


# base_url = 'https://apigw.nfex.io' # mainnet
base_url = 'https://apigw-uat.nfexinsider.com' # nfex local testnet


def sign(path, values={}):
    timestamp = str(int(time.time() * 1000))
    # hash message for signing, request by their API
    msg = ''
    if values: # POST request
        msg = f'method=POST&path={path}&timestamp={timestamp}&access-key={api_key}&body={values}'
    else: # GET request
        msg = f'method=GET&path={path}&timestamp={timestamp}&access-key={api_key}'
    hash_msg = hmac.new(bytes.fromhex(api_key), msg.encode(), hashlib.sha256)

    # sign message
    private_key = os.getenv('PRIVATE_KEY')
    signature = SigningKey(bytes.fromhex(private_key)).sign(hash_msg.digest())

    # API headers
    return {
        'API-KEY': api_key,
        'TIMESTAMP': timestamp,
        'SIGN': signature.hex()
    }


# non-stop looping until keyboard interrupt
while True:

    # get mark price
    path = f'/market/ticker?trade_pair_id={trade_pair_id}'
    headers = sign(path)
    res = requests.get(base_url + path, headers=headers)
    res_json = res.json()
    mark_price = res_json['data']['fp']
    print('Mark price:', mark_price)

    # calculate offer price
    offer_price = float(mark_price) * 102 / 100 # add 2%
    print('Offer price:', offer_price)

    # submit offer
    path = '/trade/order'
    values = {
        'amount': size,
        'o_type': 'limit',
        'o_way': 3, # 1 - open long, 2 - open and close short, 3 - open short, 4 - open long positions
        'position_type': 2, # 1 - isolated margin, 2 - cross margin
        'symbol_id': trade_pair_id,
        'lever': 10, # TODO: minimum leverage is 10 for testnet, please change to 5 in mainnet
        'price': offer_price
    }
    values = json.dumps(values)
    headers = sign(path, values)
    res = requests.post(base_url + path, headers=headers, data=values)
    res_json = res.json()

    # pretty print response
    res_pretty = json.dumps(res_json, indent=1)
    print_json(res_pretty)

    # wait for refresh_seconds and repeat
    time.sleep(refresh_seconds)
