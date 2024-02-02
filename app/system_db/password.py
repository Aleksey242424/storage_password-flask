from app.system_db import db_session
from datetime import datetime


class Password:
    @staticmethod
    def add(title,password,user_id):
        from app.system_db.models import Password
        with db_session() as session:
            session.add(Password(title=title,password=password,user_id=user_id,date_create=datetime.utcnow()))
            session.commit()
    
    @staticmethod
    def update(title,password,user_id):
        from app.system_db.models import Password
        with db_session() as session:
            instance = session.query(Password).filter_by(title=title,password=password,user_id=user_id).scalar()
            instance.title = title
            instance.password = password
            session.commit()

    @staticmethod
    def get(user_id,page):
        from app.system_db.models import Password
        with db_session() as session:
            data = session.query(Password).filter_by(user_id=user_id).order_by(Password.password_id.desc()).offset(5*page-5).limit(5)
            return data
        
    @staticmethod
    def get_password(password_id):
        from app.system_db.models import Password
        with db_session() as session:
            password_data = session.query(Password).filter_by(password_id=password_id).scalar()
            return password_data
        
    @staticmethod
    def update_password_data(password_id,password_,title):
        from app.system_db.models import Password
        with db_session() as session:
            password = session.query(Password).filter_by(password_id=password_id).scalar()
            password.password = password_
            password.title = title
            session.commit()

    @staticmethod
    def get_count_group(user_id):
        from app.system_db.models import Password
        with db_session() as session:
            count_password = session.query(Password).filter_by(user_id=user_id).count()
            return int(-1*(count_password/5)//1*-1)
 
