from models.User import User


class UserRepository:
    def __init__(self, db):
        self.db = db
    
    def add_user(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
    
    def remove_user(self, user_id: str) -> bool:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        return True

    def get_by_id(self, user_id: str) -> User:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def find_user_by_username(self, username:str) -> str:
        user = self.db.query(User).filter(User.username == username).first()
        if user:
            return user.id
        return None
    
    def get_all_users(self) -> list[User]:
        return self.db.query(User).all()




