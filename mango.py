
import asyncio

from mango_explorer_v4.mango_client import MangoClient


async def main():
    symbol = "SOL-PERP"
    depth = 2

   

    mango_client = await MangoClient.connect()

    print(await mango_client.orderbook_l2(symbol,depth))

if __name__ == '__main__':
    asyncio.run(main())