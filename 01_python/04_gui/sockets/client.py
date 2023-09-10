#!/usr/bin/env python3
""" Simple sockets client """

import socket
import threading
import argparse


def task1(_id, msg, addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((addr, port))
    except ConnectionRefusedError:
        print("Connection refused")
        return

    msg = "Client: {}, msg: {}".format(_id, msg)
    sock.send(msg.encode('utf-8'))

    msg = sock.recv(1024).decode('utf-8')
    print(msg, f'- client {_id}')

    sock.close()


def ThreadsType(arg):
    """ArgParser argument type"""
    try:
        value = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer")

    if value < 1:
        raise argparse.ArgumentTypeError("Must be greater than or equal 1")
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--message", '-m', type=str,
                        help="The message to send", default="Hello world")
    parser.add_argument('--address', '-a', type=str, help="Server address",
                        default="127.0.0.1")
    parser.add_argument('--port', '-p', type=int, help="Server port",
                        default=5000)
    parser.add_argument('--threads', '-t', type=ThreadsType,
                        help="Number of threads", default=1)
    args = parser.parse_args()

    threads = []

    for i in range(args.threads):
        thread = threading.Thread(target=task1, args=(
            i, args.message, args.address, args.port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
