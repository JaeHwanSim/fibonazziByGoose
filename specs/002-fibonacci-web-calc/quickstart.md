# Quickstart: Fibonacci Web Calculator

## 1. Prerequisites
- Python 3.10+
- An active Python virtual environment.

## 2. Development Setup
1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the backend server**:
   From the `backend` directory, run:
   ```bash
   uvicorn src.main:app --reload
   ```
4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000`.

## 3. Running Tests
From the `backend` directory, run:
- **Run all tests**:
  ```bash
  pytest
  ```
- **Run only unit tests**:
  ```bash
  pytest tests/unit
  ```
- **Run only integration tests**:
  ```bash
  pytest tests/integration
  ```

## 4. Feature Flow
1. A user accesses the `index.html` page in their browser.
2. The `script.js` file validates the input and calls the `/api/calculate` endpoint.
3. The FastAPI backend uses the `FibonacciCalculator` class to perform the calculation.
4. The result is returned as JSON and rendered on the frontend.
