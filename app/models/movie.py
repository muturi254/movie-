class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self, id, title, overview, image, vote_avarage, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.image = image
        self.vote_avarage = vote_avarage
        self.vote_count = vote_count