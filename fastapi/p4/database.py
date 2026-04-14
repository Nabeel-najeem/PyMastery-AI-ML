from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url =  "postgresql://postgres:123@localhost:5432/project_1"
engine = create_engine(db_url)
Session = sessionmaker(autocommit = False,autoflush=False,bind=engine)