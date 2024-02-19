"""create auth model

Revision ID: fe4ecb865f98
Revises: 
Create Date: 2024-02-18 18:34:20.292880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe4ecb865f98'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  # Create auth schema
  op.execute(sa.DDL(
  """
    CREATE SCHEMA auth;
  """
  ))

  # Create users table
  op.execute(sa.DDL(
  """
    CREATE TABLE auth.users (
      id SERIAL PRIMARY KEY,
      username VARCHAR UNIQUE,
      password VARCHAR,
      name VARCHAR,
      last_name VARCHAR,
      email VARCHAR,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))

  # Create access_tokens table
  op.execute(sa.DDL(
  """
    CREATE TABLE auth.access_tokens (
      access_token VARCHAR primary key,
      user_id INTEGER,
      created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  """
  ))


def downgrade() -> None:
  op.execute(sa.DDL("DROP TABLE auth.access_tokens;"))
  op.execute(sa.DDL("DROP TABLE auth.users;"))
  op.execute(sa.DDL("DROP SCHEMA IF EXISTS auth CASCADE;"))
