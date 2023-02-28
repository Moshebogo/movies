class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def get_title(self):
        return self.title

    def get_reviews(self):
        return self.reviews
          
    def get_viewers(self):
        return [review.viewer for review in self.reviews]

    def average_rating(self):
        return (sum(review.rating for review in self.reviews) / len(self.reviews) )

    def highest_review(self):
        return (max(self.reviews, key=lambda review:review.rating))        

class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def get_username(self):
        return self.username

    def get_reviews(self):
        return self.reviews

    def get_movies(self):
        return [review.movie for review in self.reviews]    

    def has_reviewed(self, movie):
        return movie in self.get_movies()
                
    def rate_movie(self, movie, rating):    
        self.reviews.append(Review(self, movie, rating))

class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    def get_rating(self):
        return self.rating

    def get_viewer(self):
        return self.viewer

    def get_movie(self):
        return self.movie