'''
Created on 15 juin 2014

@author: sylvainmougel
'''


#!/usr/bin/python           # This is client.py file

import socket               # Import socket module


def start():
    s = socket.socket()         # Create a socket object
    host = '192.168.0.20' # Get local machine name
    port = 12345                # Reserve a port for your service.

    s.connect((host, port))
    print s.recv(1024)
    s.close                     # Close the socket when done

if __name__ == '__main__':
    start()