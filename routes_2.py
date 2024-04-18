from flask import Flask, request
from marshmallow import ValidationError
from models import Base, engine, session, get_all_users, add_user, User
from schemas import UserSchema
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route("/api/users/<int:id>")
class UserManage(Resource):
    @api.doc(responses={200: 'Success', 404: 'User not found'}, params={'id': 'User ID'})
    def get(self, id):
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
        return {'user_data': user_data}

    @api.doc(responses={200: 'Success', 404: 'User not found', 500: 'Internal Server Error'},
             params={'id': 'User ID'}, body=UserSchema)
    def put(self, id):
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
        schema = UserSchema()
        return schema.dump(get_all_users()), 200

    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, body=UserSchema)
    def post(self):
        data = request.json
        print(data)
        schema = UserSchema()
        try:
            user = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        user = add_user(user)
        return schema.dump(user), 201


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)
