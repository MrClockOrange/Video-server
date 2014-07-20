#!/usr/bin/python
import socket               # Import socket module
import os
import util
import threading
import subprocess
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



def launch():
    print subprocess.Popen(["omxplayer", "-o local", "/home/pi/data/movies/Game.Of.Thrones.S04E09.FASTSUB.VOSTFR.720p.HDTV.x264-F4ST.mkv"], stdout=subprocess.PIPE).stdout.read()


class Server(threading.Thread):
    
    def __init__(self, port, movie_dir):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket()         # Create a socket object
        self.stop = False
        self.dir = movie_dir
    
    def end(self):
        print 'Close socket'
        self.sock.close()
        self.stop = True
        
        
    def run(self):
        try:
            self.sock.bind(('', self.port))        # Bind to the port
        
            self.sock.listen(5)                 # Now wait for client connection.
            while not self.stop:
                print "Wait for a connection"
                c, addr = self.sock.accept()     # Establish connection with client.
                task = c.recv(8)
                print 'Got connection from', addr, 'action to do', task
                if task == 'END':
                    self.end()
                elif task == 'MOVIES':
                    bytes_send = c.send((str(Movies(get_movies(self.dir)).get_names())))
                    print bytes_send
                elif task == 'LAUNCH':
                    bytes_send = c.send(str(launch()))
                    print bytes_send
                    
                c.close()    
                # Close the connection
                
            print "Quit server thread"
        except:
            raise



if __name__ == '__main__':
    s = Server(12345, movies_dir)
    s.start()
