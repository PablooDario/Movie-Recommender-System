from pydantic import BaseModel
from datetime import date
from typing import Optional, List


class MovieResponse(BaseModel):
    id: int
    tmdb_id: Optional[int] = None
    title: str
    genres: Optional[List[str]] = None
    overview: Optional[str] = None
    release_date: Optional[date] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    runtime: Optional[int] = None
    tagline: Optional[str] = None
    director: Optional[str] = None
    cast: Optional[List[str]] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None

    class Config:
        from_attributes = True