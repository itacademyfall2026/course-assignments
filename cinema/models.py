from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.orm import registry
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey


mapper_registry = registry()


@mapper_registry.mapped_as_dataclass
class Movie:
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    poster: Mapped[str]
    tag: Mapped[str | None] # то же самое, что и mapped_column(nullable=True)
    country: Mapped[str]
    country_flag: Mapped[str]
    duration_minutes: Mapped[int]
    genres: Mapped[list[str]] = mapped_column(JSON)
    director: Mapped[str]
    top_cast: Mapped[list[str]] = mapped_column(JSON)
    synopsis: Mapped[str] = mapped_column(Text)
    trailer_id: Mapped[str] = mapped_column(String(22))
    screenings: Mapped[list["Screening"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
        repr=False,
    )
    age_rating: Mapped[str] = mapped_column(default="0+")
    format: Mapped[str] = mapped_column(String(2), default="2D")


@mapper_registry.mapped_as_dataclass
class Hall:
    __tablename__ = "halls"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    image: Mapped[str]
    seats: Mapped[list["Seat"]] = relationship(
        back_populates="hall",
        cascade="all, delete-orphan",
        repr=False,
    )
    screenings: Mapped[list["Screening"]] = relationship(
        back_populates="hall",
        cascade="all, delete-orphan",
        repr=False,
    )


@mapper_registry.mapped_as_dataclass
class Seat:
    __tablename__ = "seats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    row: Mapped[int]
    number: Mapped[int]
    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id", ondelete="CASCADE"))
    hall: Mapped[Hall] = relationship(back_populates="seats")
    tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="seat",
        cascade="all, delete-orphan",
        repr=False,
    )


@mapper_registry.mapped_as_dataclass
class Screening:
    __tablename__ = "screenings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id", ondelete="CASCADE"))
    movie: Mapped[Movie] = relationship(back_populates="screenings", repr=False)
    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id", ondelete="CASCADE"))
    hall: Mapped[Hall] = relationship(back_populates="screenings", repr=False)
    start: Mapped[datetime]
    tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="screening",
        cascade="all, delete-orphan",
        repr=False,
    )

@mapper_registry.mapped_as_dataclass
class Ticket:
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    screening_id: Mapped[int] = mapped_column(ForeignKey("screenings.id", ondelete="CASCADE"))
    screening: Mapped[Screening] = relationship(back_populates="tickets", repr=False)
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id", ondelete="CASCADE"))
    seat: Mapped[Seat] = relationship(back_populates="tickets", repr=False)
