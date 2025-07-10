# FastAPI Project

This is a simple FastAPI project that uses `uvicorn` as the ASGI server.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)
- Required Python libraries:
  - `fastapi`
  - `uvicorn`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

Running the Application
1. Start the FastAPI application using uvicorn:

uvicorn main:app --reload

Replace main:app with the correct module and application instance if different.

2. Open your browser and navigate to:

http://127.0.0.1:8000

3. Access the interactive API documentation at:

http://127.0.0.1:8000/docs

Testing the API
Use tools like curl, Postman, or the built-in Swagger UI at /docs to test the API endpoints.

License
This project is licensed under the MIT License.