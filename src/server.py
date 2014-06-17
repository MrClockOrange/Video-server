#!/usr/bin/python
import socket               # Import socket module
import os
from os.path import isdir, isfile, join

movies_dir = '/home/pi/data/movies'




class Movie(object):
    
    def __init__(self, name, path):
        self.name = name
        self.path = path


class Movies(object):
    extension = ('avi', 'mkv', 'mp4')
    
    def __init__(self, path):
        movie_list = []
        


def get_movies(path):
    """
    return the list of all the movie under a given path
    """
    movies_list = []
    
    for f in os.listdir(movies_dir):
        
        if isdir(join(path,f)):
            movies_list.extend(get_movies(join(path,f)))
        elif isfile(join(path,f)):
            movies_list.append(f) 
            
    return movies_list
    

def start():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname()
    print host
    port = 12345                # Reserve a port for your service
    s.bind(('', port))        # Bind to the port
    
    s.listen(5)                 # Now wait for client connection.
    while True:
        print "Wait for a connection"
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        c.send(str(get_movies(movies_dir)))
        c.close()                # Close the connection



if __name__ == '__main__':
    start()
