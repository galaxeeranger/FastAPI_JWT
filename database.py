from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mysql_url_database = "mysql+pymysql://root:hell@localhost:3306/fast_db"

engine = create_engine(mysql_url_database)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
