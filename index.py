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
from phrases import get_phrases

values = {}

## ================================================== user interact section ==================================================

## API base url
# base_url = 'https://apigw.nfex.io' # mainnet
base_url = 'https://apigw-uat.nfexinsider.com' # nfex local testnet

## 用户(Account)

## 资产列表(asset list)
path = '/account/assets'

## 资金流水(account bills)
## action: 1 - 开多手续费, 2 - 开空手续费, 3 - 平多手续费, 4 - 平空手续费, 5 - 平多赢亏, 6 - 平空赢亏
## action: 1 - Fee for long opening, 2 - Fee for short opening, 3 - Fee for closing long, 4 - Fee for closing short, 5 - Fee for closing long, 6 - Profit and loss for closing
## can choose multiple action i.e. '1,2,3' (without space)
# action = '' # leave blank to view all; above action (copy from api docs) return nothing
# begin_time = ''
# coin_code = ''
# end_time = ''
# page_num = '' # 当前页(page num)
# page_size = '' # 每页条数(page size)
# path = f'/account/bills?action={action}&begin_time={begin_time}&coin_code={coin_code}&end_time={end_time}&page_num={page_num}&page_size={page_size}'

## 查询订单委托(query order)
# begin_time = ''
# end_time = ''
# order_ids = ''
# order_status = 'Pending' # possible values: Pending, Finished
# page_num = '1' # 当前页(page num)
# page_size = '1000' # 每页条数(page size)
# trade_pair_id = ''
# path = f'/account/orders?begin_time={begin_time}&end_time={end_time}&order_ids={order_ids}&order_status={order_status}&page_num={page_num}&page_size={page_size}&trade_pair_id={trade_pair_id}'

## 获取仓位(get a position)
# path = '/account/positions'

## other possible account path
# path = '/account/orderData'
# path = '/account/fee'
# path = '/account/info'
# path = '/account/withdrawList'


## 市场(market)

## 获取深度(get depth)
# trade_pair_id='1002' # required
# trade_pair_name='' # optional, can leave blank
# path = f'/market/depth?trade_pair_id={trade_pair_id}&trade_pair_name={trade_pair_name}'

## 单个交易对的ticker(ticker for a single trading pair)
# trade_pair_id='1002' # required
# trade_pair_name='' # optional, can leave blank
# path = f'/market/ticker?trade_pair_id={trade_pair_id}&trade_pair_name={trade_pair_name}'

## 所有交易对的ticker(ticker for all trading pair)
# path = '/market/tickers'

## other possible market path
# path = '/market/pairs?enable=2&visible=2'


## 委托单(orders)

# path = '/trade/order'
# values = """
# {
#     "amount": "0.001",
#     "o_type": "limit",
#     "o_way": 1,
#     "position_type": 2,
#     "symbol_id": 1002,
#     "lever": 20,
#     "price": "1"
# }
# """

## possible input
## amount: required, 订单额(order amount)
## o_type: required, 订单类型(order type) "limit" or "market"
## o_way: required, 委托方向(order entrustment direction) 1 - 开多(open long) 2 - 平空(Open and close short) 3 - 开空(open short) 4 - 平多(open long positions)
## position_type: required, 仓位类型(position type) 1 - 逐仓(isolated Margin) 2 - 全仓(cross Margin)
## o_mode: 订单模式(order mode) 1 - 普通(ordinary) 7 - 止赢(take profit) 8 - 止损(stop loss)
## symbol_id: 交易对id(trade pair id)
## vol: 订单量(order quantity)
## custom_id: 客户端定义的id(client defined id)
## lever: 杠杆(lever)
## position_id: 仓位id(position id)
## price: 价格(price)
## strategy: 订单策略(order strategy) GTC - 一直有效至取消(valid until canceled)

## multiple orders in single API call is possible by
## 1. change path to '/trade/orders'
## 2. change values to:
##   values = """{ "orders": [order_1, order_2, order_3] }""""
##   where content for each order_ is same as values above
##   { "amount": "0.001", "o_type": "limit", ... }

## ================================================== end of user interact section ==================================================


timestamp = str(int(time.time() * 1000))
api_key = "d202565e3bd8c4d4b6bdd21c4e1133ef3f6ab7c6fc6b638cbe2d4d7d05460c9c"

# hash message for signing, request by their API
method = ''
msg = ''
if values: # POST request
    method = 'POST'
    msg = f'method=POST&path={path}&timestamp={timestamp}&access-key={api_key}&body={values}'
else: # GET request
    method = 'GET'
    msg = f'method=GET&path={path}&timestamp={timestamp}&access-key={api_key}'
hash_msg = hmac.new(bytes.fromhex(api_key), msg.encode(), hashlib.sha256)

# sign message
private_key = os.getenv("PRIVATE_KEY")
signature = SigningKey(bytes.fromhex(private_key)).sign(hash_msg.digest())

# API header
headers = {
    'API-KEY': api_key,
    'TIMESTAMP': timestamp,
    'SIGN': signature.hex()
}

# request API
res = ''
if method == 'GET':
    res = requests.get(base_url + path, headers=headers)
else: # method = 'POST'
    res = requests.post(base_url + path, headers=headers, data=values)
res_json = res.json()

# this section replace key in symbol with human readable text
# comment out this if want to see original symbol
if "data" in res_json:
    res_json['data'] = get_phrases(res_json['data'])

# pretty print response
res_pretty = json.dumps(res_json, indent=1)
print_json(res_pretty)
