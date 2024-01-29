from app.system_db import db_session


class Password:
    @staticmethod
    def add(title,password,user_id):
        from app.system_db.models import Password
        with db_session() as session:
            session.add(Password(title=title,password=password,user_id=user_id))
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
            data = session.query(Password).filter_by(user_id=user_id).all()
            return data

 
