#!/usr/bin/python
'''
Created on 10 juin 2014

@author: sylvainmougel
'''
'''
Created on 10 juin 2014

@author: sylvainmougel
'''

import socket               # Import socket module




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
        c.send('Thank you for connecting')
        c.close()                # Close the connection



if __name__ == '__main__':
    start()
