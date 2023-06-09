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

3. Create a `.env` file and insert `PRIVATE_KEY=private key here`

4. Edit input in === user interact section === and run script
> python3 bot.py

## api.py

Examples to call NFEX API

> python3 api.py

## trade id - name

### main env

1001 - AZUKI/ETH

1002 - BAYC/ETH

1003 - MAYC/ETH

1004 - CLONEX/ETH

1005 - MOONBI/ETH

1006 - DOODLE/ETH

1007 - PENGUI/ETH

1008 - NAKAMI/ETH

1009 - OTHERD/ETH

1010 - PUNKS/ETH

1011 - DEGODS/ETH

1012 - MILADY/ETH

1013 - KODA/ETH

1014 - CAPT/ETH

1015 - POTATO/ETH

1016 - BAKC/ETH

1017 - BEANZ/ETH

1018 - PIXELM/ETH

1019 - MEEBIT/ETH

1021 - REMILI/ETH

1024 - KUBZ/ETH

1026 - MFERS/ETH

### test env

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

## ed25519 keypair

This script generate random keypair for ed25519 locally, which contain public key & private key of ed25519 for the API.

> python3 keypair.py

Public key to give NFEX team, together with EOA that reload ETH, for whitelist purpose.

Private key to insert into `.env` file to use the API, after NFEX team whitelisted successfully.

## UI Url

Main: https://www.nfex.io/trade/BAYC

Test: https://web-uat.nfexinsider.com/trade/BAYC

API docs in nfex-api.html
