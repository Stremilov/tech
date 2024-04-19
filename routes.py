from flask import Flask, request
from models import Base, engine, session, User
from schemas import UserSchema
from flask_restx import Resource, Api

import structlog
import logging

app = Flask(__name__)
api = Api(app)


logging.basicConfig(format="%(levelname)-8s [%(asctime)s] %(message)s", level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)
struct_logger = structlog.getLogger()


@api.route("/api/users/<int:id>")
class UserManage(Resource):
    """
    Get, update, delete user
    """
    @api.doc(responses={200: 'Success', 404: 'User not found'}, params={'id': 'User ID'})
    def get(self, id):
        """
        Function displays complete user information
        """
        user_ids = [data[0] for data in session.query(User.id).all()]
        user_data = None
        if id in user_ids:
            user_row = session.query(User.username, User.email, User.registration_date).filter_by(id=id).first()
            registration_date_str = user_row.registration_date.strftime('%Y-%m-%d %H:%M:%S')
            user_data = {
                'username': user_row.username,
                'email': user_row.email,
                'registration_date': registration_date_str
            }
            return {'user_data': user_data}, 200
        else:
            return {"status": 404}

    @api.doc(responses={200: 'Success', 404: 'User not found', 500: 'Internal Server Error'},
             params={'id': 'User ID'}, body=UserSchema)
    def put(self, id):
        """
        Function updates user data
        """
        data = request.json
        user = session.query(User).get(id)
        if user:
            try:
                user.username = data.get('username', user.username)
                user.email = data.get('email', user.email)
                session.commit()
                return {"message": "User updated successfully"}, 200
            except Exception as e:
                session.rollback()
                return {"error": str(e)}, 500
        else:
            return {"error": "User not found"}, 404

    @api.doc(responses={200: 'Success', 404: 'User not found', 500: 'Internal Server Error'},
             params={'id': 'User ID'})
    def delete(self, id):
        """
        Function deletes user
        """
        user = session.query(User).get(id)
        if user:
            try:
                session.delete(user)
                session.commit()
                return {"message": "User deleted successfully"}, 200
            except Exception as e:
                session.rollback()
                return {"error": str(e)}, 500
        else:
            return {"error": "User not found"}, 404


@api.route("/api/users")
class UsersList(Resource):

    @api.doc(responses={200: 'Success'})
    def get(self):
        # здесь можно юзануть схему
        """
        Function gets all users
        """
        users = session.query(User).all()
        user_list = []
        for user in users:
            registration_date_str = user.registration_date.strftime('%Y-%m-%d %H:%M:%S')
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'registration_time': registration_date_str
            }
            user_list.append(user_dict)
        return user_list

    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, body=UserSchema)
    def post(self):
        # и здесь можно юзануть схему
        """
        Function add to DB new user
        """
        data = request.json
        try:
            user = User(username=data['username'], email=data['email'])
            session.add(user)
            session.commit()
            return {"status": "done"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)
