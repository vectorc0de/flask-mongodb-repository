# Job Board API

A simple and powerful RESTful API to manage job postings, built with Flask, MongoDB, and MongoEngine.

## Features

- **Create, Read, Update, and Delete (CRUD)** operations for job postings.
- Built with **Flask** and **MongoEngine**.
- Uses the **Repository Pattern** for clean and maintainable code.
- Includes **Unit Tests** with mocking.
- **CI/CD** with GitHub Actions.
- Easy to set up and run.

## Project Structure

```
.
├── .github
│   └── workflows
│       └── main.yml
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── repositories.py
│   └── routes.py
├── tests
│   └── test_app.py
├── README.md
├── requirements.txt
└── run.py
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/vectorc0de/fastapi-mongodb-repository.git
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the application

To run the application, execute the following command:

```bash
python run.py
```

The application will be running on `http://127.0.0.1:5000`.

## Running the tests

To run the tests, execute the following command:

```bash
python -m unittest discover tests
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/jobs/` | Creates a new job posting. |
| `GET` | `/jobs/` | Retrieves all job postings. |
| `GET` | `/jobs/<job_id>` | Retrieves a specific job posting. |
| `PUT` | `/jobs/<job_id>` | Updates a specific job posting. |
| `DELETE` | `/jobs/<job_id>` | Deletes a specific job posting. |

## Continuous Integration

This project uses [GitHub Actions](https://github.com/features/actions) for Continuous Integration. The workflow is defined in `.github/workflows/main.yml`.

Every time you push to the `main` branch or create a pull request to `main`, the following actions will be performed:

1.  The code will be checked out.
2.  Python will be set up.
3.  The dependencies will be installed.
4.  The tests will be run.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [MongoEngine](http://mongoengine.org/) - The Object-Document Mapper (ODM) for MongoDB.
- [MongoDB](https://www.mongodb.com/) - The NoSQL database.