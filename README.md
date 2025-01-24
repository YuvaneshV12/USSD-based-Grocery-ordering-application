# USSD-based-Grocery-ordering-application

This project is a Flask-based USSD application that allows users to browse categories (Food, Groceries, Fruits) and add items to their cart using a USSD-like interface.

## Features
- Dynamic menu navigation for category and item selection.
- Item addition to a cart based on the user's phone number.
- Basic error handling for invalid selections and inputs.

## Prerequisites
1. Python 3.7 or higher
2. Flask library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ussd-food-grocery.git
    cd ussd-food-grocery
    ```

2. Install the required Python libraries:
    ```bash
    pip install flask
    ```

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Test the USSD app by sending POST requests to the `/ussd` endpoint using tools like Postman or cURL:
    - **Endpoint:** `http://127.0.0.1:5000/ussd`
    - **Method:** POST
    - **Form Data:**
      - `sessionId`: Any unique session ID (e.g., `12345`).
      - `serviceCode`: Any service code (e.g., `*123#`).
      - `phoneNumber`: A user phone number (e.g., `+123456789`).
      - `text`: User input (e.g., `1` for Food).

3. Follow the menu prompts based on your input.
