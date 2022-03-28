#!/bin/python3

import socket
from termcolor import colored 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter IP Address of Target: ")

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored("Port {} is Closed".format(port),'red'))
    else:
        print("Port {} is Open. ".format(port))

for port in range(1,1000):
    portscanner(port)
