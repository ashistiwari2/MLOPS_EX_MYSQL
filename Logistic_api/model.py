from sqlalchemy import Column,Float,String,Integer
from Logistic_api.database import Base
class logistic_api(Base):
    __tablename__='logistic_api'
    id=Column(Integer,primary_key=True,index=True)
    Weight =Column(Float)
    Length1= Column(Float)
    Length2= Column(Float)
    Length3=Column(Float)
    Height=Column(Float)
    Width=Column(Float)
    Species=Column(String(16))

