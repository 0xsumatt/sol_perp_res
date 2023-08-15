import httpx

import pandas as pd

data = {
    "API_KEY": "zxMTJr3MHk7GbFUCmcFyFV4WjiDAufDp",
    "pairName": "SOL-PERP"
}

req = httpx.post("https://api-services.goosefx.io/perps-apis/getOrderBook",json=data).json()
bids = req['bids']
asks = req['asks']
max_len = max(len(bids), len(asks))
bids += [None] * (max_len - len(bids))
asks += [None] * (max_len - len(asks))

df = pd.DataFrame({
    'bid price': [bid['price'] if bid is not None else float('nan') for bid in bids],
    'bid size': [bid['size'] if bid is not None else float('nan') for bid in bids],
    'ask price': [ask['price'] if ask is not None else float('nan') for ask in asks],
    'ask size': [ask['size'] if ask is not None else float('nan') for ask in asks],
    'token': ['SOL'] * max_len
})
column_order = ['bid price', 'bid size', 'ask price', 'ask size', 'token']
df = df[column_order]

print(df)










