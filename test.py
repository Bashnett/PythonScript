#!/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter IP Address to Scan: ")

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port {} is Closed".format(port))
    else:
        print("Port {} is Open".format(port))
for port in range(1, 1000):
    portscanner(port)
