# Kitten Exhibition API

Welcome to the Kitten Exhibition API! This project is a RESTful API built using Django and Django Rest Framework (DRF) that allows users to manage and showcase their kittens. The API includes features for creating, updating, and deleting kitten entries, as well as handling user authentication with JWT.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)

## Features

- User registration and authentication using JWT.
- CRUD operations for kitten entries.
- Ability to filter kittens by breed.
- User permissions to ensure users can only modify their own kittens.
- Ranking for kittens

## Technologies Used

- Django
- Django Rest Framework
- PostgreSQL
- pytest for testing
- Docker for containerization

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.12 (for development purposes)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rahmet97/KittenInfoProject.git
   cd KittenInfoProject

Create a .env file in the root directory and define the necessary environment variables, for example:

    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password

### Running the Application

Build and run the Docker containers:

    docker-compose up --build

After the containers are up, the API will be accessible at http://localhost:8000/swagger.

To run database migrations and load initial data, the application will do this automatically when starting.

### Running Tests

To run the tests, use the following command:

    docker-compose run web pytest

This command will execute all tests in the api/tests.py file.
API Endpoints

    POST /auth/register/: User registration.
    POST /auth/login/: User login, returns JWT.
    GET /api/kittens/: List all kittens.
    GET /api/kittens/?breed_id=3: Filter kittens by breed.
    POST /api/kittens/: Create a new kitten.
    GET /api/kittens/{id}/: Retrieve a specific kitten.
    PUT /api/kittens/{id}/: Update a specific kitten.
    PATCH /api/kittens/{id}/: Update a specific kitten partially.
    DELETE /api/kittens/{id}/: Delete a specific kitten.
    GET /api/ratings/: Get ratings of kittens.
    GET /api/ratings/?kitten_id=1: Filter ratings by kitten.
    POST /api/ratings/: Give marks to kittens.
