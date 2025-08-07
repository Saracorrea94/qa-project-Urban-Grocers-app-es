🛒 API Testing Project - URBAN GROCERS

🚀 Project Overview

This project automates testing for the Urban Grocers API, an application that allows users to manage custom kits.
The main goal is to validate the creation of kits through the corresponding endpoint, focusing specifically on different input scenarios for the name field in the request body.

The tests ensure the API handles various cases correctly, including:

Minimum and maximum character length validations

Special character inclusion

Missing name field

Invalid data types

📚 Documentation Source

The API documentation was accessed via apiDoc at:
https://cnt-101beed5-59ed-4630-a31b-512ed1ea1f59.containerhub.tripleten-services.com/docs/

💻 Technologies Used

Python 3.x

Pytest for running automated test cases

Requests library for HTTP API calls

Modular programming: reusable and organized code across files like configuration.py, data.py, and sender_stand_request.py

Best practices in automated testing, including separation of positive and negative test cases


👩‍💼 Key Responsibilities

Designed and developed automated tests for the create_kit endpoint with a focus on input validation for the name field

Structured test coverage into positive and negative test cases to ensure comprehensive validation

Created reusable functions for API requests to improve code maintainability

Used parameterized inputs to efficiently test edge cases and boundary conditions


🚀 Impact & Achievements

Improved test efficiency by using modular and reusable code components

Identified inconsistencies in API behavior when handling invalid inputs

Established a clean structure for scalable test case additions in future iterations


⚙️ Requirements

Before running the project, make sure you have:

Python 3.x installed

Terminal or command line access

A code editor (e.g., PyCharm)

Git configured (optional, if uploading to GitHub)


📦 Installing Dependencies
To install required libraries, run:

bash
Copiar
Editar
pip install requests
pip install pytest

📁 Project Structure

graphql
Copiar
Editar
qa-project-Urban-Grocers-app-en/
├── configuration.py             # URL and endpoint configuration
├── data.py                      # Data and headers for requests
├── sender_stand_request.py      # Functions to send API requests
└── create_kit_name_kit_test.py  # Automated test cases using Pytest

▶️ How to Run the Tests

Open a terminal and navigate to the root folder of the project. Example:

bash
Copiar
Editar
cd C:/Users/sarac/projects/qa-project-Urban-Grocers-app-en
Make sure pytest is installed. If not, install it with:

bash
Copiar
Editar
pip install pytest
To run all test files in the project, use:

bash
Copiar
Editar
pytest .
This will automatically detect and run all test files matching the pattern test_*.py or *_test.py.

To run a specific test file, such as create_kit_name_kit_test.py, use:

bash
Copiar
Editar
pytest create_kit_name_kit_test.py
To get more detailed output, add the verbose flag:

bash
Copiar
Editar
pytest -v

👤 Author

Developed by Sara Correa
TripleTen QA Engineer Bootcamp Graduate
