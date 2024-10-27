# Learning Management System (LMS) API



## Table of Contents
- [Project Overview](#overview)
- [Technologies Used](#tech-stack)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [License](#license)
- [Contact](#contact)

## Overview

The Learning Management System (LMS) is a robust Django REST API designed to facilitate the management of courses, user registrations, enrollments, and role-based access control. The API enables seamless interactions between instructors, students, and administrators, allowing them to efficiently perform various actions such as course creation, assignment submission, and grading.


## Tech Stack

- **Backend Framework**: Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JSON Web Tokens (JWT)

## Features

- **User Management**: Role-based access control for instructors, students, and administrators.
- **Course Management**: Create, update, delete, and retrieve courses.
- **Enrollment Management**: Enroll users in courses and track their progress.
- **Assignment Management**: Instructors can create assignments and grade submissions.
- **Secure Authentication**: JWT-based authentication for secure user sessions.

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/lms.git
   cd lms

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Configure Database Settings**
    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
    }
5. **Apply Migrations**
    ```bash
    python manage.py migrate

6. **Run the Development Server**
    ```bash
    python manage.py runserver

## Usage
Once the server is running, you can interact with the API using tools like Postman or CURL. Ensure you include the JWT token in your request headers for authentication.

## API Documentation
You can access the API documentation via /docs after running the server.


## License
This project is licensed under the MIT License

## Contact
For any inquiries, please contact:

- Brian Omondi: brianhilsden@gmail.com
- GitHub: [brianhilsden](https://github.com/brianhilsden)