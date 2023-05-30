# NFEX API

## bot.py

This simple bot fetch mark price from API, add 2% on top of it and posts new order.

The order is limit order, open short, cross margin and leverage 5x (in testnet 10x minimum)

X seconds after posts new order, it again fetch mark price from API, add 2% on top of it and posts new order.

The process will repeat until interrupt by keyboard.

1. Create Python environment
> python3 -m venv env

2. Activate the environment
> source env/bin/activate

3. Install dependencies
> pip install -r requirements.txt

3. Insert private key in `.env` file

4. Edit input in === user interact section === and run script
> python3 bot.py

## api.py

Examples to call NFEX API

> python3 api.py

## UI Url

Main: https://www.nfex.io/trade/BAYC

Test: https://web-uat.nfexinsider.com/trade/BAYC

API docs in nfex-api.html
