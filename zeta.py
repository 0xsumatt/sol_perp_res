import pandas as pd
import httpx

req = httpx.get("https://dex-mainnet-webserver-ecs.zeta.markets/orderbooks?marketIndexes[]=137").json()

dfs = []
for token, orders in req['orderbooks'].items():
    bids = []
    asks = []
    for order in orders:
        if 'bids' in order:
            bids.extend(order['bids'])
        if 'asks' in order:
            asks.extend(order['asks'])
    max_len = max(len(bids), len(asks))
    bids = bids + [None] * (max_len - len(bids))
    asks = asks + [None] * (max_len - len(asks))
    token_df = pd.DataFrame({
        'bid price': [bid['price'] if bid is not None else None for bid in bids],
        'bid size': [bid['size'] if bid is not None else None for bid in bids],
        'ask price': [ask['price'] if ask is not None else None for ask in asks],
        'ask size': [ask['size'] if ask is not None else None for ask in asks],
        'token': [token] * max_len
    })
    dfs.append(token_df)

result_df = pd.concat(dfs, ignore_index=True)
filtered_df = result_df.query("token == 'SOL'")
print(filtered_df)
