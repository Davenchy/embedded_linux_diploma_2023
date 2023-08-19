#!/usr/bin/env python3
"""Get the public ip address of the machine"""
import requests

IP_INFO_ENDPOINT = "https://api.ipify.org/?format=json"


def get_ip_info():
    """Get the public ip address of the machine

    Returns: str|None"""
    res = requests.get(IP_INFO_ENDPOINT)
    if res.status_code != 200:
        return None

    data = res.json()
    return data['ip']


if __name__ == "__main__":
    ip = get_ip_info()
    if ip is None:
        print("Failed to fetch data")
        exit(1)

    print(ip)
