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
o_way = 1 # order entrustment direction, 1 - open long, 2 - close short, 3 - open short, 4 - close long
size = '0.005'
refresh_seconds = 5 # 5 seconds
api_key = 'd202565e3bd8c4d4b6bdd21c4e1133ef3f6ab7c6fc6b638cbe2d4d7d05460c9c'
spread = -0.02
leverage = 10

## =============================================== end of user interact section ===============================================


# base_url = 'https://apigw.nfex.io' # mainnet
base_url = 'https://apigw-uat.nfexinsider.com' # nfex local testnet
order_id = ''


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

    # cancel order if any
    if order_id:
        print('Cancelling order...')
        path = '/trade/cancelOrders'
        values = {
            'orders': [order_id],
            'symbol_id': trade_pair_id
        }

        values = json.dumps(values)
        headers = sign(path, values)
        res = requests.post(base_url + path, headers=headers, data=values)
        res_json = res.json()
        res_pretty = json.dumps(res_json, indent=1)
        print_json(res_pretty)
        print('')


    # get mark price
    print('Getting mark price...')
    path = f'/market/ticker?trade_pair_id={trade_pair_id}'
    headers = sign(path)
    res = requests.get(base_url + path, headers=headers)
    res_json = res.json()
    mark_price = res_json['data']['fp']
    print('Mark price:', mark_price)

    # calculate offer price
    offer_price = float(mark_price) * (1+spread)
    print('Offer price:', offer_price)
    print('')

    # submit offer
    print('Submitting new order...')
    path = '/trade/order'
    values = {
        'amount': size,
        'o_type': 'limit',
        'o_way': o_way,
        'position_type': 2, # 1 - isolated margin, 2 - cross margin
        'symbol_id': trade_pair_id,
        'lever': leverage,
        'price': offer_price
    }

    values = json.dumps(values)
    headers = sign(path, values)
    res = requests.post(base_url + path, headers=headers, data=values)
    res_json = res.json()
    order_id = res_json['data']['order_id']
    symbol_id = res_json['data']['symbol_id']

    # pretty print response
    res_pretty = json.dumps(res_json, indent=1)
    print_json(res_pretty)
    print('')

    # wait for refresh_seconds and repeat
    print(f'Wait for {refresh_seconds} seconds...')
    time.sleep(refresh_seconds)
