#!/usr/bin/env python3
# Simple login system
from getpass import getpass


def validate(credentials, username, password):
    """Check if username is a key in credentials 
    and its value is the same as the password

    Args:
        credentials(dict): A dictionary has username/password as a key/value
        username(str): the username to look for as a key of credentials
        password(str): the password to look for as a value to an exist key in
        credentials
    """
    return username in credentials.keys() and credentials[username] == password


if __name__ == "__main__":
    credentials = {
        "Ahmed": "1394",
        "Ali": "6078",
        "Amr": "9345",
        "Davenchy": "123456"
    }

    while 1:
        username = input("> Enter username: ")
        if not username:
            break

        password = getpass("> Enter password: ")

        if validate(credentials, username, password):
            print(f"Welcome, {username.capitalize()}!")
            break
        else:
            print("Incorrect credentials")
            print("Try again or enter nothing to quit\n")
