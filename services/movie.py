from models.movie import Movie as MovieModel

class MovieService():
    def __init__(self,db)->None:
        self.db = db
    
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie_by_id(self,id):
        result = self.db.query(MovieModel).filter(MovieModel.id==id).first()
        return result
    
    def filter_movies_by_category(self,category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).first()
        return result