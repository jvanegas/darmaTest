from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

# TODO: add default values
config = {
  "DATABASE_ENGINE": os.getenv("DATABASE_ENGINE"),
  "DATABASE_USER": os.getenv("DATABASE_USER"),
  "DATABASE_PASSWORD": os.getenv("DATABASE_PASSWORD"),
  "DATABASE_DB": os.getenv("DATABASE_DB"),
  "DATABASE_PORT": os.getenv("DATABASE_PORT"),
  "DATABASE_HOST": os.getenv("DATABASE_HOST"),
  "REDIS_HOST": os.getenv("REDIS_HOST"),
  "REDIS_PORT": os.getenv("REDIS_PORT"),
  "DEBUG": os.getenv("DEBUG"),
  "LOG_LEVEL": os.getenv("LOG_LEVEL"),
  "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY")
}
