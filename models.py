from typing import List, Type

from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///tech.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    registration_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}, {self.username}, {self.email}, {self.registration_date}"


def get_all_users() -> List[dict]:
    users = session.query(User).all()
    user_list = []
    for user in users:
        registration_date_str = user.registration_date.strftime('%Y-%m-%d %H:%M:%S')
        user_dict = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'registration_time': registration_date_str  # Преобразование времени в строку в формате ISO
        }
        user_list.append(user_dict)
    return user_list


def add_user(user: User):
    try:
        new_user = User(username=user.username, email=user.email)
        session.add(new_user)
        session.commit()
        return {"message": "User created successfully"}, 201
    except IntegrityError:
        session.rollback()
        return {"error": "Username or email already exists"}, 400
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 500

