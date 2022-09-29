from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib

# SQLALCHEMY_DATABASE_URL = "sqlite:///./logistic.db"
host_server = os.environ.get('host_server', ' 127.0.0.1')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '3306')))
database_name = os.environ.get('database_name', 'fastapi_app')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'ashistiwari2')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', '1234567890@At')))
SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(db_username,db_password,host_server,db_server_port,database_name)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,pool_size=3, max_overflow=0
    #connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#dbname='{your_database}' user='ashistiwari2@fastapi-machine-learning-api' host='fastapi-machine-learning-api.postgres.database.azure.com' password='{your_password}' port='5432' sslmode='true'
