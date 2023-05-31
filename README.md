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

## trade id - name

1001 - AZUKI/ETH

1003 - MAYC/ETH

1004 - CLONEX/ETH

1006 - DOODLE/ETH

1008 - OTHERD/ETH

1009 - PUNK/ETH

1010 - NAKAMI/ETH

1012 - DEGODS/ETH

1013 - MILADY/ETH

1018 - BAKC/ETH

1019 - BEANZ/ETH

1022 - GEMESIS/ETH

1023 - LFPEPE/ETH

1027 - REMILI/ETH

1029 - KPANDA/ETH

1031 - KUBZ/ETH

1032 - 0N1/ETH

1033 - MFERS/ETH

1034 - OPEPEN/ETH

## UI Url

Main: https://www.nfex.io/trade/BAYC

Test: https://web-uat.nfexinsider.com/trade/BAYC

API docs in nfex-api.html
