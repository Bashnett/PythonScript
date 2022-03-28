#!/bin/python3

import socket
from termcolor import colored 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Enter IP Address to Scan: ")
#port = int(input("[*] Enter the port to Scan"))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored("Port {} is Closed".format(port), 'red'))
    else:
        print(colored("Port{} is Open".format(port), 'blue'))

for port in range(1,1000):
    portscanner(port)
