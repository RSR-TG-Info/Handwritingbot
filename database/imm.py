
from config import Config
from database.database import Database

rsr = Database(Config.DATABASE_URL, Config.DATABASE_NAME)
