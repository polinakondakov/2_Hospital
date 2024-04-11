from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_HOST, DB_PORT, DB_PASSWORD, DB_USER, DB_NAME

Base = declarative_base() #Создается базовый класс Base, который будет использоваться для определения моделей базы данных
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=False)
get_session = sessionmaker(engine, autocommit=False)
print(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")