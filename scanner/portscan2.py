#!/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter ip Address: ")
port = int(input("[*] Enter port of ip Address: "))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port {} is Open.".format(port))
    else:
        print("Port {} is Close.".format(port))
portscanner(port)
