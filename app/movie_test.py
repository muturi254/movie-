import unittest
from .models import movie # remve period to test

# get the class in movies
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''class to test movie '''
    def setUp(self):
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series',
                               'https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs', 8.5, 129993)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

if __name__ == '__main__':
    unittest.main()