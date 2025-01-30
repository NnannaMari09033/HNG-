# HNG API Project

A public API built with Django to retrieve basic information. This project provides a simple, scalable way to access basic data via a `GET` request, returning the response as a JSON object with a status code of `200 OK`.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

The **HNG API** is a public API developed with Django that allows users to retrieve basic information using a `GET` request. The API is designed to return a well-structured JSON response with the relevant data and a status code of `200 OK` upon success.

---

## Installation

To set up this project locally, follow these instructions.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NnannaMari09033/HNG-.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd hng-api
    ```

3. **Create and activate a virtual environment:**

    - For macOS/Linux:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

    - For Windows:

    ```bash
    python -m venv myenv
    myenv\Scripts\activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

    ```

6. **Run the server:**

    ```bash
    python manage.py runserver
    ```

The server will now be running at `http://127.0.0.1:8080/`.

---

## Usage

To use the API, simply run the Django development server with the following command:

```bash
python manage.py runserver
The API will be available at the base URL:

API Endpoints
1. GET /api/
Description: Retrieves a list of basic information from the system.
Request: GET /api/
Response: A JSON object containing the requested information.
json

{
  "data": [
    {
      "id": 1,
      "name": "Sample Data 1",
      "info": "This is a sample data object."
    },
    {
      "id": 2,
      "name": "Sample Data 2",
      "info": "This is another sample data object."
    }
  ]
}
Response Status Code: 200 OK
Example Request
You can make a GET request to the /api/ endpoint using tools like Postman 
