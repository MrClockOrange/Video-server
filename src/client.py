#!/usr/bin/python           # This is client.py file

'''
Created on 15 juin 2014

'''

import socket               # Import socket module


def start():
    s = socket.socket()         # Create a socket object
    host = 'raspberrypi'        # Get local machine name
    port = 12345                # Reserve a port for your service.
    packet_list = []
    s.connect((host, port))
    while 1:
        pack = s.recv(1024)
        if len(pack) > 0:
            packet_list.append(pack)
        else:
            break
    s.close                     # Close the socket when done
    
    movie_list =  '.'.join(packet_list).split(',')
    for movie in movie_list:
        print movie

if __name__ == '__main__':
    start()