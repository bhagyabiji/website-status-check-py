
# Python Website Status Checker

A beginner-friendly Python tool that checks website HTTP responses and displays their status codes.

## Features

- Check one or multiple websites
- Automatically add HTTPS when no scheme is provided
- Display HTTP status codes
- Identify successful responses, redirects, client errors, and server errors
- Handle timeouts and connection errors
- Validate basic URL structure


## Technologies Used

- Python 3
- Requests library
- urllib.parse

## Installation

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install the required dependency:

   python -m pip install -r requirements.txt

## How to Run

Run the following command:

    python main.py

Enter one or more website URLs separated by commas.

Example:

    https://example.com, https://python.org

## Example Output

    Website: https://example.com
    HTTP Status Code: 200
    Result: Website responded successfully.

Actual results depend on the website and network connection.


## Learning Outcomes

- Python functions and loops
- HTTP requests and response codes
- Exception handling
- URL parsing and validation
- Basic website availability checks

## Author

Bhagya B
