'''
Created on 25 juin 2014

'''
import unittest
import server
import client
import socket
import time



port = 12353
s = server.Server(port, '/Users/sylvainmougel/video_sync')
c = client.Client('127.0.0.1', port)

class TestClient(unittest.TestCase):


    def setUp(self):
        s.start()
       


    def tearDown(self):
        pass
       
    def testClient(self):
        c.get_movie_list()
        time.sleep(2)
        c.close_server()

        
    def testLaunch(self):
        c.lauch()
        time.sleep(2)
        c.close_server()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetMoovies']
    unittest.main()