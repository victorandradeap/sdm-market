from typing import List, Optional, Dict
from flask import abort
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.user import User
from app.schemas.user import user_schema

class UserAlreadyExistsError(Exception):
    "Raised when attempting to create a user with an email that already exists in the database."
    pass

class UserService:
    def __init__(self, database=None):
        self.db = database or db

    def create_user(self, data) -> User:
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            raise UserAlreadyExistsError(f"User with email {data['email']} already exists")

        new_user = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        
        self.db.session.add(new_user)
        try:
            self.db.session.commit()
            return new_user
        except Exception as e:
            self.db.session.rollback()
            raise e

    def get_all_users(self) -> List[User]:
        return User.query.all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = User.query.get(user_id)
        if not user:
            abort(404, description="User not found")
        return user

    def update_user(self, user_id: int, name: str) -> User:
        user = self.get_user_by_id(user_id)
        user.name = name
        try:
            self.db.session.commit()
            return user
        except Exception as e:
            self.db.session.rollback()
            raise e

    def delete_user(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        try:
            self.db.session.delete(user)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e