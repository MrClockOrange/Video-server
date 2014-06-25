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
        movies = server.Movies(server.get_movies('/Users/sylvainmougel/video_sync'))
        
        for m in movies.movie_list:
            print m.get_name()

        print movies.get_names()
        
        self.failIf(movies.get_len() != 55)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetMoovies']
    unittest.main()