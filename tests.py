from unittest import TestCase
from datetime import datetime
from models import Base, User
from models import app, session, engine


class TestUserEndpoints(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        Base.metadata.create_all(engine)
        self.client = app.test_client()
        self.add_sample_users()

    def tearDown(self):
        session.remove()
        Base.metadata.drop_all(engine)

    def add_sample_users(self):
        user1 = User(username='user1', email='user1@example.com', registration_date=datetime.utcnow())
        session.add(user1)
        session.commit()

    def test_get_user(self):
        response = self.client.get('/api/users/1')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data

    def test_get_user_not_found(self):
        response = self.client.get('/api/users/999')
        self.assertEqual(response.status_code, 404)

    # Add more test methods for other endpoints (PUT, DELETE, POST)
