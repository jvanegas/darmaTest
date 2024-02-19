"""seed DB

Revision ID: f47a6a5dd99a
Revises: e0b0923fa69c
Create Date: 2024-02-18 19:05:38.105462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f47a6a5dd99a'
down_revision: Union[str, None] = 'e0b0923fa69c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  # Create users
  op.execute(
    """
      INSERT INTO auth.users (id, username, password, name, last_name)
      VALUES 
      (1, 'darma', 'pass1234', 'Darma', 'AI'),
      (2, 'alice.thomson', 'pass1234', 'Alice', 'Thomson'),
      (3, 'bob.power', 'pass1234', 'Bob', 'Power');
    """
  )

  # Create guardians
  op.execute(
    """
      INSERT INTO activity.guardians (user_id, name, last_name, email)
      VALUES 
      (1, 'Darma', 'AI', 'darma@test.com'),
      (2, 'Alice', 'Thomson', 'alice@test.com'),
      (3, 'Bob', 'Power', 'bob@test.com');
    """
  )

  # Create families
  op.execute(
    """
      INSERT INTO activity.families (id, family_name)
      VALUES 
      (1, 'Darma Family'),
      (2, 'Alice and Bob Family');
    """
  )

  # Create children
  op.execute(
    """
      INSERT INTO activity.children (id, full_name, family_id)
      VALUES 
      (1, 'Little Darma', 1),
      (2, 'Little Alice', 2);
    """
  )

  # Create family_members
  op.execute(
    """
      INSERT INTO activity.family_members (id, guardian_id, family_id, children_id, relationship_type)
      VALUES 
      (1, 1, 1, 1, 'parent'),
      (2, 2, 2, 2, 'parent'),
      (3, 3, 2, 2, 'parent');
    """
  )

def downgrade() -> None:
  op.execute("DELETE FROM auth.users;")
  op.execute("DELETE FROM activity.guardians;")
  op.execute("DELETE FROM activity.families;")
  op.execute("DELETE FROM activity.children;")
  op.execute("DELETE FROM activity.family_members;")
