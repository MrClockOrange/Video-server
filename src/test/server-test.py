'''
Created on 25 juin 2014

'''
import unittest
import server


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testGetMoovies(self):
        movies = server.get_movies('/Users/sylvainmougel/video_sync')
        self.failIf(len(movies) == 3)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetMoovies']
    unittest.main()