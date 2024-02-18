from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import os

engine = os.getenv("DATABASE_ENGINE", "postgresql")
dbUser = os.getenv("DATABASE_USER", "postgres")
dbPassword = os.getenv("DATABASE_PASSWORD", "postgres")
dbHost = os.getenv("DATABASE_HOST", "localhost")
dbPort = os.getenv("DATABASE_PORT", "5432")
dbName = os.getenv("DATABASE_DB", "postgres")

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername=engine,
    username=dbUser,
    password=dbPassword,
    host=dbHost,
    port=dbPort,
    database=dbName,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=MetaData(schema="family_activity"))
