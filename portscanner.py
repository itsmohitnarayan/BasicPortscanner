#!usr/bin/python3

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please Enter the IP :")
port = int(input("Please Enter the port :"))


def portscanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portscanner(port)
    
