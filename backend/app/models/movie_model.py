from sqlalchemy import Integer, String, Date, Text, JSON, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.db.session import Base


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tmdb_id: Mapped[int | None] = mapped_column(Integer, unique=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    genres: Mapped[list | None] = mapped_column(JSON)
    overview: Mapped[str | None] = mapped_column(Text)
    release_date: Mapped[date | None] = mapped_column(Date)
    vote_average: Mapped[float | None] = mapped_column(DECIMAL(3, 2))
    vote_count: Mapped[int | None] = mapped_column(Integer)
    runtime: Mapped[int | None] = mapped_column(Integer)
    tagline: Mapped[str | None] = mapped_column(String(256))
    director: Mapped[str | None] = mapped_column(String(64))
    cast: Mapped[list | None] = mapped_column(JSON)
    poster_path: Mapped[str | None] = mapped_column(String(64))
    backdrop_path: Mapped[str | None] = mapped_column(String(64))

    # Relationships: one movie has many ratings
    ratings: Mapped[list["Rating"]] = relationship("Rating", back_populates="movie")

    def __repr__(self) -> str:
        return f"<Movie id={self.id} title='{self.title}'>"