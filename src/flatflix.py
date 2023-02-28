class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def get_title(self):
        return self.title

    def get_reviews(self):
        return self.reviews
          

    def get_viewers(self):
        viewers = []
        for review in self.reviews:
            viewers.append(review.viewer)
        return viewers  

    def average_rating(self):
        return (sum(review.rating for review in self.reviews) / len(self.reviews) )

    def highest_review(self):
        highest = self.reviews[0]
        for review in self.reviews:
            if review.rating > highest.rating:
                highest = review
        return highest         


class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def get_username(self):
        return self.username

    def get_reviews(self):
        return self.reviews

    def get_movies(self):
        movies = []
        for review in self.reviews:
            movies.append(review.movie)
        return movies     

    def has_reviewed(self, movie):
        for review in self.reviews:
            if movie == review.movie:
                return True
                
    



    def rate_movie(self, movie, rating):
        new_review = Review(self, movie, rating)
        self.reviews.append(new_review)


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