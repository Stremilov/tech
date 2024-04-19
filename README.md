User Management REST API

This project aims to develop a REST API for managing a list of users using a database. The API will provide endpoints to perform CRUD (Create, Read, Update, Delete) operations on user records stored in the database.

## Features

- Create User: Allow the creation of new user records by providing necessary details such as username and email.
- Read User: Retrieve user information by either querying all users or fetching a specific user by their unique identifier.
- Update User: Update user details like username or email for a particular user.
- Delete User: Remove a user from the system based on their ID.

## Technologies Used

- Flask: Python web framework for building the REST API endpoints.
- SQLite: Lightweight relational database management system for storing user data.
- RESTful API: Conforming to REST principles for designing the API endpoints.
- HTTP Methods: Using POST, GET, PUT, and DELETE methods for performing CRUD operations.

## Getting Started

1. Clone the repository to your local machine.
2. Install the required dependencies by running pip install -r requirements.txt.
3. Set up the database connection details in the configuration file.
4. Run the Flask application using python app.py.
5. Access the API endpoints to interact with the user management system.

## Endpoints

- POST /api/users: Create a new user by providing username and email.
- GET /api/users: Retrieve all users in the database.
- GET /api/users/{id}: Fetch a specific user by their ID.
- PUT /api/users/{id}: Update user details such as username or email.
- DELETE /api/users/{id}: Delete a user from the system by their ID.

## Implementation Details

- The Flask web application serves as the backend for the API.
- User data is stored and managed using a SQLite database.
- Unit tests are provided in the tests.py file to ensure the functionality of the API endpoints.



# Routes.py 

This file contains the routes for interacting with the User resource in the API.

## Setup
- Import necessary libraries and modules.
- Set up Flask app and create an instance of Api.
- Configure logging for the application using structlog.

## UserManage Resource
- Route: /api/users/<int:id>
- Methods: GET, PUT, DELETE
- GET: Retrieves complete user information based on user ID.
- PUT: Updates user data based on user ID.
- DELETE: Deletes a user from the database.

## UsersList Resource
- Route: /api/users
- Methods: GET, POST
- GET: Retrieves all users from the database.
- POST: Adds a new user to the database.

## Running the Application
- If the file is run directly, it creates the necessary database tables.
- The application runs in debug mode.

# models.py

This file defines the database models and operations related to the User resource in the API.

## Setup
- Import necessary libraries and modules for defining database models and operations.
- Set up the Flask app instance and create a database engine with SQLAlchemy.

## User Model
- Define a SQLAlchemy model named User with columns for id, username, email, and registration_date.
- Override the __repr__ method to provide a formatted representation of the User object.

## Operations
- get_all_users: Fetch all users from the database and return a list of dictionaries containing user information.
- add_user: Add a new user to the database, handling integrity constraints for unique username and email fields.

## Running the Application
- Ensure the database connection is established before using the models and operations defined in this file.
- The file can be imported and used in other parts of the application to interact with user data in the database.

# schemas.py

This file defines data validation schemas using Marshmallow for the User resource in the API.

## Setup
- Import necessary libraries and modules for defining data validation schemas.
- Import the User model from the models module (though not used in the current implementation).

## UserSchema
- Define a schema using Marshmallow for validating and serializing User data.
- Include fields for id, username, email, and registration_time.
- Implement validation logic for email and username fields to check for uniqueness in the database.

## Validation Methods
- create_user: Post-processing method to create a User object from validated data.
- validate_email: Ensure email uniqueness in the database when validating email field data.
- validate_username: Ensure username uniqueness in the database when validating username field data.

This file provides a structured way to validate and serialize User data, although it may need a database session to interact with User records for validation.

# tests.py

This file contains unit tests for the API endpoints related to user management.

## Setup
- Import necessary libraries for testing and interacting with the Flask application.
- Import the Flask app from the routes module for testing endpoints.

## User Management Test Cases
- TestUserManage: Test case class for user management operations.
  - test_add_user: Test adding a new user using a POST request.
  - test_get_all_users: Test fetching all users using a GET request.
  - test_get_user: Test fetching a specific user by ID using a GET request.
  - test_update_user_by_username: Test updating a user's username using a PUT request.
  - test_update_user_by_email: Test updating a user's email using a PUT request.
  - test_update_user_by_username_and_email: Test updating a user's username and email using a PUT request.

## User Deletion Test Cases
- TestUserDelete: Test case class for user deletion operations.
  - test_delete_user: Test deleting a user by ID using a DELETE request.
  - test_delete_user_fail: Test case to simulate a failed user deletion request (expecting a 404 response).

## Running the Tests
- Each test method sends requests to the API endpoints and asserts the expected response status codes.
- Test cases can be executed to ensure the proper functionality of the user management endpoints.

Ensure that the Flask application is running and accessible for these tests to interact with the defined API endpoints.
