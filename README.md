# User CRUD Hexagonal Architecture

This project is a Python FastAPI application implementing a user CRUD system using hexagonal architecture. This was created for my own personal understanding.


### Project Structure

```
user_crud_hex/
├── app/
│   ├── main.py          # Entry point of the application
│   ├── models/          # Data models
│   ├── routes/          # API routes
│   ├── services/        # Business logic
│   └── repositories/    # Data access layer
├── tests/               # Unit and integration tests
├── venv/                # Virtual environment
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```


## Getting Started

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Setup

1. **Clone the Repository**  
    ```bash
    git clone <repository-url>
    cd user_crud_hex
    ```

2. **Create a Virtual Environment**  
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**  
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the FastAPI Server**  
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Access the API Documentation**  
    Open your browser and navigate to:  
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.