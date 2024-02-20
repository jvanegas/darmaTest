"""create family activity model

Revision ID: e0b0923fa69c
Revises: fe4ecb865f98
Create Date: 2024-02-18 18:34:39.223938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0b0923fa69c'
down_revision: Union[str, None] = 'fe4ecb865f98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  # Create activity schema
  op.execute(sa.DDL(
  """
    CREATE SCHEMA activity;
  """
  ))

  # Create guardians table
  op.execute(sa.DDL(
  """
    CREATE TABLE activity.guardians (
      user_id INTEGER PRIMARY KEY,
      name VARCHAR,
      last_name VARCHAR,
      email VARCHAR,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))

  # Create families table
  op.execute(sa.DDL(
  """
    CREATE TABLE activity.families (
      id INTEGER PRIMARY KEY,
      family_name VARCHAR,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))

  # Create children table
  op.execute(sa.DDL(
  """
    CREATE TABLE activity.children (
      id SERIAL PRIMARY KEY,
      full_name VARCHAR,
      family_id INTEGER,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))

  # Create family_members table
  op.execute(sa.DDL(
  """
    CREATE TABLE activity.family_members (
      id INTEGER PRIMARY KEY,
      guardian_id INTEGER,
      children_id INTEGER,
      family_id INTEGER,
      relationship_type VARCHAR,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))

  # Create activities table
  op.execute(sa.DDL(
  """
    CREATE TABLE activity.activities (
      id SERIAL PRIMARY KEY,
      child_id INTEGER,
      family_id INTEGER,
      activity_name VARCHAR,
      activity_weekday INTEGER,
      activity_start_time TIME WITH TIME ZONE,
      activity_end_time TIME WITH TIME ZONE,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))

  # Create activities_history table
  op.execute(sa.DDL(
  """
    CREATE TABLE activity.activities_history (
      id SERIAL PRIMARY KEY,
      activity_id Integer,
      responsible_guardian_id INTEGER,
      is_completed BOOLEAN,
      resolved_at TIMESTAMP WITHOUT TIME ZONE,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))


def downgrade() -> None:
  op.execute(sa.DDL("DROP TABLE activity.family_members;"))
  op.execute(sa.DDL("DROP TABLE activity.guardians;"))
  op.execute(sa.DDL("DROP TABLE activity.children;"))
  op.execute(sa.DDL("DROP TABLE activity.families;"))
  op.execute(sa.DDL("DROP TABLE activity.activities;"))
  op.execute(sa.DDL("DROP TABLE activity.activities_history;"))
  op.execute(sa.DDL("DROP SCHEMA IF EXISTS activity CASCADE;"))
