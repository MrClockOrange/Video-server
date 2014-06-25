#!/usr/bin/python
import socket               # Import socket module
import os
import util
from os.path import isdir, isfile, join

movies_dir = '/home/pi/data/movies'


class Movie(object):
    
    def __init__(self, name, full_path):
        self.ext = name[-3:]
        self.name = name[:-4]
        self.full_path = full_path
    
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

class Movies(object):
    
    def __init__(self, movies):
        self.movie_list = movies
        self.names = []
        for m in movies:
            self.names.append(m.get_name())

    def get_len(self):
        return len(self.movie_list)

    def get_names(self):
        return self.names
    


def get_movies(path):
    """
    return the list of all the movie under a given path
    """
    movies_list = []
    
    
    for f in os.listdir(path):
        
        full_file_path = join(path,f)
        if isdir(full_file_path):
            
            movies_list.extend( get_movies(full_file_path) )
            
        elif isfile(full_file_path) and full_file_path[-3:] in util.extension:
            m = Movie(f, full_file_path)
            movies_list.append(m)
    
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
        bytes_send = c.send((str(Movies(get_movies(movies_dir)).get_names())))
        print bytes_send
        c.close()                # Close the connection



if __name__ == '__main__':
    start()
