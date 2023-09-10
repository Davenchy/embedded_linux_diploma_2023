#!/usr/bin/env python3
""" Simple sockets server """

import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--address", '-a', type=str, help="Server address",
                        default="127.0.0.1")
    parser.add_argument('--port', '-p', type=int, help="Server port",
                        default=5000)
    parser.add_argument('--message', '-m', type=str,
                        help="The message to send to the client",
                        default="Hello from server")
    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((args.address, args.port))
    sock.listen()
    print("Listening on port", args.port)

    try:
        while True:
            conn, addr = sock.accept()
            print("Connected by", addr)
            data = conn.recv(1024)
            conn.send(args.message.encode('utf-8'))
            print(f"Received ({addr}):", data.decode('utf-8'))
            print('==========================')
            conn.close()
    except KeyboardInterrupt:
        pass
