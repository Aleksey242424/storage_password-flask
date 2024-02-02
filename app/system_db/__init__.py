from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,scoped_session,sessionmaker
from app import login
from config import Config

engine = create_engine(url=f'postgresql+{Config.DB_API}://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}')

Base = declarative_base()

db_session = scoped_session(sessionmaker(bind=engine,autoflush=False,autocommit=False,expire_on_commit=False))



@login.user_loader
def get_user(user_id):
    from app.system_db.models import Users
    return Users.query.get(user_id)