from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib

# SQLALCHEMY_DATABASE_URL = "sqlite:///./logistic.db"
# host_server = os.environ.get('host_server', 'fastapi-machine-learning-api.postgres.database.azure.com')
# db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
# database_name = os.environ.get('database_name', 'fastapi')
# db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'ashistiwari2@fastapi-machine-learning-api')))
# db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', '1234567890@At')))
# ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
# SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
host_server = os.environ.get('host_server', 'machine-learning-api.mysql.database.azure.com')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '3306')))
database_name = os.environ.get('database_name', 'fastapi_app')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'ashistiwari2@machine-learning-api')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', '1234567890@At')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(db_username,db_password,host_server,db_server_port,database_name)
#mysql.connector.connect(user="ashistiwari2@machine-learning-api", password='1234567890@At', host="machine-learning-api.mysql.database.azure.com", port=3306, database="fastapi_app")
# ssl_ca={ca-cert filename}, ssl_verify_cert=true)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,pool_size=3, max_overflow=0
    #connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#dbname='{your_database}' user='ashistiwari2@fastapi-machine-learning-api' host='fastapi-machine-learning-api.postgres.database.azure.com' password='{your_password}' port='5432' sslmode='true'