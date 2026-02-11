import random
from sqlalchemy.orm import Session
from app.models import Movie


class MovieService:
    def __init__(self, db: Session):
        self.db = db

    def get_movie_by_id(self, movie_id: int) -> Movie | None:
        return self.db.query(Movie).filter(Movie.id == movie_id).first()

    def get_popular_movies(self) -> list[Movie]:
        movies = (
            self.db.query(Movie)
            .where(Movie.vote_count >= 10000)
            .order_by(Movie.vote_average.desc())
            .limit(30)
            .all()
        )
        
        return random.sample(movies, 20)
