import json
import unittest
from time import sleep

from routes import app


class TestUserManage(unittest.TestCase):
    """
    Testing endpoints
    """

    def test_add_user(self):
        """
        Adding user test
        """
        with app.test_client() as client:
            response = client.post('/api/users', data=json.dumps({"username": "testClient", "email": "testEmail"}),
                                   content_type='application/json')
            self.assertEqual(response.status_code, 201)

    def test_get_all_users(self):
        """
        Get all users test
        """
        with app.test_client() as client:
            response = client.get('/api/users')
            self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        """
        Test to get current user
        """
        with app.test_client() as client:
            response = client.get('/api/users/1')
            self.assertEqual(response.status_code, 200)

    def test_update_user_by_username(self):
        """
        Test to update username
        """
        with app.test_client() as client:
            response = client.put('/api/users/1', data=json.dumps({"username": "qwe"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_update_user_by_email(self):
        """
        Test to update email
        """
        with app.test_client() as client:
            response = client.put('/api/users/1', data=json.dumps({"email": "testUser@gmail.com"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_update_user_by_username_and_email(self):
        """
        Test to update username and email
        """
        with app.test_client() as client:
            response = client.put('/api/users/1', data=json.dumps({"username": "qwe", "email": "testUser@gmail.com"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)


class TestUserDelete(unittest.TestCase):

    def test_delete_user(self):
        """
        Test delete user
        """
        with app.test_client() as client:
            response = client.delete('/api/users/1')
            self.assertEqual(response.status_code, 200)

    def test_delete_user_fail(self):
        """
        Test delete user (fail)
        """
        with app.test_client() as client:
            response = client.delete('/api/users/1')
            self.assertEqual(response.status_code, 404)
