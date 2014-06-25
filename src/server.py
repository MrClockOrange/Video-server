#!/usr/bin/python
import socket               # Import socket module
import os
import util
from os.path import isdir, isfile, join

movies_dir = '/home/pi/data/movies'


class Movie(object):
    
    def __init__(self, name, full_path):
        self.ext = name[-3:]
        self.name = name[:-3]
        self.full_path = full_path
    
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

class Movies(object):
    
    def __init__(self, path):
        self.movie_list = []
    
    def add(self, movie):
        self.movie_list.append(movie)

        
        




def get_movies(path):
    """
    return the list of all the movie under a given path
    """
    movies_list = []
    
    
    print "call get movie with path :" + path
    
    for f in os.listdir(path):
        
        full_file_path = join(path,f)
        if isdir(full_file_path):
            
            print "dir :" + full_file_path
            movies_list.extend( get_movies(full_file_path) )
            
        elif isfile(full_file_path) and full_file_path[-3:] in util.extension:
            Movie(f, full_file_path)
            movies_list.append(Movie)
    print movies_list
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
        bytes_send = c.send(str(get_movies(movies_dir)))
        print bytes_send
        c.close()                # Close the connection



if __name__ == '__main__':
    start()
