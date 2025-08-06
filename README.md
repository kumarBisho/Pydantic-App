# Pydantic App

Pydantic App is a Python project demonstrating the use of Pydantic for data validation and FastAPI for building web APIs. This project is structured for learning and experimentation with modern Python tools and best practices.

## Features
- FastAPI-based web application
- Pydantic models for robust data validation
- Environment configuration using pydantic-settings and python-dotenv
- Ready for deployment with Uvicorn

## Project Structure
```
main.py                # Entry point for the application
pyproject.toml         # Project metadata and dependencies
README.md              # Project documentation
uv.lock                # Dependency lock file
01-foundation/
  examples/            # FastAPI and Pydantic usage examples
    fastapi.py
    field_example.py
    first_model.py
    nested_model.py
    pydantic_serialization.py
    user_validator.py
  solutions/           # Solutions to modeling exercises
    course_model_solution.py
    employee_model_solution.py
    hotel_booking_solution.py
    product_model_soltion.py
```

## Getting Started
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or use Poetry:
   ```bash
   poetry install
   ```
2. **Run the application**:
   ```bash
   python main.py
   ```
   Or, if using FastAPI and Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## Requirements
- Python >= 3.13
- FastAPI
- Pydantic
- pydantic-settings
- python-dotenv
- Uvicorn

## License
This project is for educational purposes.
