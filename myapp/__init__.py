import uuid

from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __tablename__ = 'BaseModel'
    __table_args__ = {'extend_existing': True}
    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    pass


engine = create_engine("mysql://root:taolavu18112005@localhost/crawlProjDB", pool_pre_ping=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
