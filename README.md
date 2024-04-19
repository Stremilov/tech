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
