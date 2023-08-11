#!/usr/bin/env python3
# Find the rate of bitcoin
import requests

ENDPOINT = "https://api.coindesk.com/v1/bpi/currentprice.json"

res = requests.get(ENDPOINT)
if res.status_code != 200:
    print("Failed to fetch data")
    exit(1)

data = res.json()
coin = data["bpi"]

for k, v in coin.items():
    print(f"{v['rate']} {k}")
