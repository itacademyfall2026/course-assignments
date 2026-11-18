from dataclasses import dataclass
from datetime import datetime


@dataclass
class Movie:
    id: int
    title: str
    poster: str
    tag: str | None
    age_rating: str
    country: str
    country_flag: str
    duration_minutes: int
    genres: list[str]
    format: str
    director: str
    top_cast: list[str]
    synopsis: str
    trailer_id: str


@dataclass
class Hall:
    id: int
    name: str
    description: str
    image: str
    seats: list["Seat"]


@dataclass
class Seat:
    id: int
    row: int
    number: int


@dataclass
class Screening:
    id: int
    movie: Movie
    hall: Hall
    start: datetime


@dataclass
class Ticket:
    id: int
    screening: Screening
    seat: Seat