from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_path = 'mysql+pymysql://root@localhost:3306/corylus'
engine = create_engine(db_path,
                       convert_unicode=True,
                       echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.task
    Base.metadata.create_all(bind=engine)
