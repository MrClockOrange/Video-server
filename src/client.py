#!/usr/bin/python           # This is client.py file

'''
Created on 15 juin 2014

'''

import socket               # Import socket module




class Client():
    
    @staticmethod
    def get_response(sock):
        packet_list = []
        while 1:
            pack = sock.recv(1024)
            if len(pack) > 0:
                packet_list.append(pack)
            else:
                break
        return '.'.join(packet_list)
        
    def __init__(self, host, port):
        self.host = host
        self.port = port 
            
    def get_movie_list(self):
        s = socket.socket()         # Create a socket object
        s.connect((self.host, self.port))
        s.send('MOVIES')
        movie_list =  Client.get_response(s).replace('[', '').replace(']', '').split(',')
        s.close                     # Close the socket when done
        for movie in movie_list:
            print movie
    
    def close_server(self):
        s = socket.socket()         # Create a socket object
        s.connect((self.host, self.port))
        s.send('END')
        s.close
        
    def launch(self):
        s = socket.socket()         # Create a socket object
        s.connect((self.host, self.port))
        s.send('LAUNCH')
        print Client.get_response(s)
        s.close


if __name__ == '__main__':
    c = Client('raspberrypi', 12345)
    c.get_movie_list()
    c.launch()
