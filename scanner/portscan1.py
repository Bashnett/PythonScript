#!/bin/python3

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.23.160"
port = 443

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port {} is closed.".format(port))
    else:
        print("Port {} is opened.".format(port))
portscanner(port)
