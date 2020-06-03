import json
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.exceptions import V20Error
import logging

account_id = '101-011-14995955-001'
token = '43b546aff89ed477d1c2841a0193b263-23e07b9e94639df4e20d217b02ddaa97'
api = API(access_token=token)

logging.basicConfig(
    filename="log.out",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s : %(message)s',
)


orderConf = [
    MarketOrderRequest(instrument="EUR_USD", units=100).data,
    MarketOrderRequest(instrument="UR_USD", units=100).data,
]

# client
api = API(access_token=token)

# create and process order requests
r = orders.OrderCreate(accountID=account_id, data=orderConf[0])
print("processing : {}".format(r))
print("===============================")
print(r.data)
try:
    response = api.request(r)
except V20Error as e:
    print("V20Error: {}".format(e))
else:
    print("Response: {}\n{}".format(r.status_code,
                                    json.dumps(response, indent=2)))