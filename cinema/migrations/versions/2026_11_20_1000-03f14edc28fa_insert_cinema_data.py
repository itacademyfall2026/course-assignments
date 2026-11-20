"""Insert cinema data

Revision ID: 03f14edc28fa
Revises: cf12a6f9c012
Create Date: 2026-11-20 10:00:00.459998

"""
import json
from datetime import datetime
from pathlib import Path
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03f14edc28fa'
down_revision: Union[str, Sequence[str], None] = 'cf12a6f9c012'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    data_path = Path(__file__).parent.parent.parent / "data"
    movies_table = sa.table(
        'movies',
        sa.Column('id', sa.Integer()),
        sa.Column('title', sa.String()),
        sa.Column('poster', sa.String()),
        sa.Column('tag', sa.String()),
        sa.Column('country', sa.String()),
        sa.Column('country_flag', sa.String()),
        sa.Column('duration_minutes', sa.Integer()),
        sa.Column('genres', sa.JSON()),
        sa.Column('director', sa.String()),
        sa.Column('top_cast', sa.JSON()),
        sa.Column('synopsis', sa.Text()),
        sa.Column('trailer_id', sa.String(length=22)),
        sa.Column('age_rating', sa.String()),
        sa.Column('format', sa.String(length=2)),
    )
    movies_file = data_path / "movies.json"
    op.bulk_insert(movies_table, json.load(movies_file.open()))
    halls_table = sa.table('halls',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String()),
        sa.Column('description', sa.Text()),
        sa.Column('image', sa.String()),
    )
    halls_file = data_path / "halls.json"
    op.bulk_insert(halls_table, json.load(halls_file.open()))
    seats_table = sa.table('seats',
        sa.Column('id', sa.Integer()),
        sa.Column('row', sa.Integer()),
        sa.Column('number', sa.Integer()),
        sa.Column('hall_id', sa.Integer()),
    )
    seats_file = data_path / "seats.json"
    op.bulk_insert(seats_table, json.load(seats_file.open()))
    screenings_table = sa.table('screenings',
        sa.Column('id', sa.Integer()),
        sa.Column('movie_id', sa.Integer()),
        sa.Column('hall_id', sa.Integer()),
        sa.Column('start', sa.DateTime()),
    )
    screenings_file = data_path / "screenings.json"
    screenings_data = json.load(screenings_file.open())
    for screening in screenings_data:
        screening["start"] = datetime.fromisoformat(screening["start"])
    op.bulk_insert(screenings_table, screenings_data)


def downgrade() -> None:
    op.execute("DELETE FROM screenings")
    op.execute("DELETE FROM seats")
    op.execute("DELETE FROM halls")
    op.execute("DELETE FROM movies")
