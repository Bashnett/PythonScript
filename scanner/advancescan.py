#!/bin/python3

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("[*] {} is Open".format(tgtPort))
    except:
        print("[-] Port {} is Closed".format(tgtPort))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unknown Host..{}".format(tgtHost))
    try:
        tgtname = gethostbyaddr(tgtIP)
        print("[*] Scan Results For: "+tgtName(0))
    except:
        print("[*] Scan Results for: "+tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage fo program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='tgtHost', type ='string', help='specify target host')
    parser.add_option('-p', dest='tgtPost', type ='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)

if _name_=='_main_':
    main()


