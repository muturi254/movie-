class Config:
    '''default and universal configuration for the flask app'''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''configuration for producion environment
     Args:
        Config: The parent configuration class with General configuration settings
    '''

    pass

class DevConfig(Config):
    '''configuration for develpment  environment
     Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
