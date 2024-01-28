from sqlalchemy.orm import Mapped,mapped_column
from app.system_db import Base,db_session,engine
from flask_login import UserMixin

class Users(Base,UserMixin):
    __tablename__ = 'users'
    user_id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(unique=True,nullable=False)
    email:Mapped[str] = mapped_column(unique=True,nullable=False)
    hash_password:Mapped[str] = mapped_column(nullable=False)

    def get(self):
        return self.user_id
    
    query = db_session.query_property()


Base.metadata.create_all(engine)
