from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///flask_memo.db')
Session = scoped_session(sessionmaker(bind=engine))