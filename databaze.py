from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Sukuriam duomenu baze "darbo_skelbimai"
DATABASE_URL = "sqlite:///darbo_skelbimai.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class DarboSkelbimai(Base):
    __tablename__ = "darbo_skelbimai"
    id = Column(Integer, primary_key=True, index=True)
    profesija = Column(String(255))
    imone = Column(String(255))
    atlyginimas = Column(String(255))
    atlyginimo_didis = Column(String(255))
    miestas = Column(String(255))
    data = Column(Text)


Base.metadata.create_all(bind=engine)
