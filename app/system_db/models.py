from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from app.system_db import Base,db_session,engine
from flask_login import UserMixin
from datetime import datetime

class Users(Base,UserMixin):
    __tablename__ = 'users'
    user_id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(unique=True,nullable=False)
    email:Mapped[str] = mapped_column(unique=True,nullable=False)
    hash_password:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[list['Password']]=relationship(back_populates='user')

    def get_id(self):
        return self.user_id
    
    query = db_session.query_property()

class Password(Base):
    __tablename__ = 'password'
    password_id:Mapped[int]=mapped_column(primary_key=True)
    password:Mapped[str] = mapped_column(nullable=False)
    title:Mapped[str]=mapped_column(nullable=False)
    date_create:Mapped[datetime]
    user_id:Mapped[int] = mapped_column(ForeignKey('users.user_id',ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    user:Mapped['Users'] = relationship(back_populates='password')
    


Base.metadata.create_all(engine)
